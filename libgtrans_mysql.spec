# Note that this is NOT a relocatable package
%define ver      0.2.0
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix      /usr
%define sysconfdir  /etc

Summary:        Database Access Library
Name: 		libgtrans_mysql_3_23
Version: 	%ver
Release: 	%rel
Copyright: 	Free Software Foundation
Group: 		Applications/Databases
BuildRoot: 	/var/tmp/libgtrans_mysql_3_23-%{ver}-root
Source:         libgtrans_mysql_3_23-%{ver}.tar.gz
DocDir:		%{prefix}/doc


%description

libgtrans_mysql_3_23 is a plugin for GNOME Transcript that
provides MySQL access

%prep
%setup -q

%build
# Needed for snapshot releases.
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif

if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib --sysconfdir=%sysconfdir
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib --sysconfdir=%sysconfdir
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README INSTALL THANKS
%{prefix}/*
