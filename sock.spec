Summary: Richard Stevens Sock
Name: sock
Version: 0.3.2
Release: 1
Epoch: 0
License: GPL
Group: Productivity/Networking/Web/Utilities
Source0: %{name}-%{version}.tar.gz
URL: http://www.icir.org/christian/sock.html
BuildRoot: %{_tmppath}/%{name}-root
Requires: libc.so.6 libc.so.6(GLIBC_2.0) libc.so.6(GLIBC_2.3) libnsl.so.1 rtld(GNU_HASH)

%description
Port and reworked code of Richard Stevens 'sock' utility by Christian Kreibich. From the author: In TCP/IP Illustrated Vol. 1, Richard Stevens used a program called "sock" to demonstrate the many properties of TCP/IP. Unfortunately, the book only speaks about how to use the program but does not point to a site for downloading its sources. While sock is contained in the code package accompanying UNIX Network Programming, this code is also getting dated. 

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*

%changelog
* Wed Apr 28 2008 San Dodd <dodd.san@gmail.com>
- Initial spec file
