# TODO: fix %files
Summary:	Database Access Library for MySQL
Summary(pl):	Biblioteka dostêpu do bazy danych MySQL
Name:		libgtrans_mysql_3_23
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/gtranscript/%{name}-%{version}.tar.gz
# Source0-md5:	47011d2dbd34251a60c94c5355f6fad3
URL:		http://gtranscript.sourceforge.net/
BuildRequires:	libgtrans_ifase-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgtrans_mysql_3_23 is a plugin for GNOME Transcript that provides
MySQL access.

%description -l pl
libgtrans_mysql_3_23 jest wtyczk± do GNOME Transcript dodaj±c± obs³ugê
do MySQL 3.23.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_prefix}/*
