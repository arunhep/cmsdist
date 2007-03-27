### RPM external gcc 3.2.3
## INITENV +PATH LD_LIBRARY_PATH %i/lib/32
## INITENV +PATH LD_LIBRARY_PATH %i/lib64
## BUILDIF [ $(uname) != Darwin ]
Source: ftp://ftp.fu-berlin.de/unix/gnu/%n/%n-%v/%n-%v.tar.bz2

%build
# FIXME: --enable-__cxa_atexit can't be used with gcc 3.2.3 on RH 7.3,
# enabling it causes qt's uic to die with segmentation violation half
# way down the build of qt (projecsettings.ui or something like that;
# not the first or only call to uic).  Disabling the flag removes the
# issue, so clearly the option does not work correctly on this
# platform combination.
mkdir -p obj
cd obj

if [ "`echo %v | cut -d. -f 1`" == "3" ]
then
../configure --prefix=%i --enable-languages=c,c++,f77 \
    --enable-shared # --enable-__cxa_atexit
else
../configure --prefix=%i --enable-languages=c,c++ \
    --enable-shared # --enable-__cxa_atexit
fi
make %makeprocesses bootstrap

%install
cd obj && make install
ln -s gcc %i/bin/cc
#
#
