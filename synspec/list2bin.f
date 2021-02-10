      program list2bin
c     ================
c
c     transforms an ASCII line list to a binary
c
      implicit real*8 (a-h,o-z)
      character*80 infile,outfile
c
      n=0
      read(*,*) infile
      i = len_trim(infile)
      if (infile(i-1:i) .eq. '19') then
          itype = 1
      else
          itype = 2
      endif

      outfile = infile
      outfile(i-1:i) = '11'
      write(*,*) 'reading/writing =',infile, '/', outfile
      open(19,file=infile,status='old')
      open(11,file=outfile,status='new',form='unformatted')
c
c     itype: type of the line list
c          = 0 - classical atomic line list
c          = 1 - atomic line list with Carlos' extended parameters
c          = 2 - molecular line list
c 
      if(itype.eq.0) then
   10    continue
         read(19,*,err=10,end=20) alam,anum,gf,excl,ql,excu,qu,gr,gs,gw
         write(11) alam,anum,gf,excl,ql,excu,qu,gr,gs,gw
         n=n+1
         go to 10
   20    continue
       else if(itype.eq.1) then
   30    continue
         read(19,*,err=30,end=40) alam,anum,gf,excl,ql,excu,qu,
     *        gr,gs,gw,i1,i2,i3,i4,i5,i6,i7
         write(11) alam,anum,gf,excl,ql,excu,qu,gr,gs,gw,
     *        i1,i2,i3,i4,i5,i6,i7
         n=n+1
         go to 30
   40    continue
c
       else
   50    continue
         read(19,*,err=50,end=60) alam,anum,gf,excl,gr,gs,gw
         write(11) alam,anum,gf,excl,gr,gs,gw
         n=n+1
         go to 50
   60    continue
      end if
c
      write(6,601) n, outfile
  601 format(i10,'  lines included in the binary file ',a80)
      end
