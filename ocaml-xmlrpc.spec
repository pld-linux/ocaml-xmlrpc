Summary:	XML-RPC implementation for OCaml
Summary(pl):	Implementacja XML-RPC dla OCamla
Name:		ocaml-xmlrpc
Version:	0.1.0
Release:	1
License:	LGPL/GPL
Group:		Libraries
Vendor:		Shawn Wagner <shawnw@speakeasy.org>
URL:		http://raevnos.pennmush.org/code/ocaml.html
Source0:	http://raevnos.pennmush.org/code/ocaml_xml-rpc-%{version}.tar.gz
BuildRequires:	ocaml-net-netstring-devel
BuildRequires:	ocaml-netclient-devel
BuildRequires:	ocaml-stew-devel
BuildRequires:	ocaml-pxp-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml >= 3.04-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
No main package.

%package devel
Summary:	XML-RPC implementation for OCaml - development part
Summary(pl):	Implementacja XML-RPC dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-net-netstring-devel
%requires_eq	ocaml-netclient-devel
%requires_eq	ocaml-stew-devel
%requires_eq	ocaml-pxp-devel
%requires_eq	ocaml-pcre-devel

%description devel
XML-RPC is a protocol for remotely invoking functions in different
programs (Usually on different computers) than where the calling code
is. It's a pretty simple protocol compared to others like CORBA, DCOM,
or even Java RMI. See http://www.xmlrpc.com/ for more information
about XML-RPC.

Library comes under LGPL, while oxridl tool comes under GPL.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl
XML-RPC jest protoko³em pozwalaj±cym wywo³ywaæ funkcje w innych
programach (przewa¿nie równie¿ na innych komputerach). Jest to ca³kiem
prosty protokó³ w porównaniu do CORBA, DCOM czy nawet Java RMI. Na
http://www.xmlrpc.com/ mo¿na znale¼æ wiêcej informacji na temat
XML-RPC.

Biblioteka jest rozprowadzana na zasadach LGPL, natomiast narzêdzie
oxridl -- na GPL.

Pakiet ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych
tej biblioteki.

%prep
%setup -q -n ocaml_xml-rpc-%{version}

%build
%{__make} all opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/xmlrpc
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir}
install x*.cmx $RPM_BUILD_ROOT%{_libdir}/ocaml/xmlrpc

echo >> $RPM_BUILD_ROOT%{_libdir}/ocaml/xmlrpc/META
echo 'directory = "+xmlrpc"' >> $RPM_BUILD_ROOT%{_libdir}/ocaml/xmlrpc/META
mv -f $RPM_BUILD_ROOT%{_libdir}/ocaml/xmlrpc/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/xmlrpc

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/xmlrpc/*.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ocaml/xmlrpc/*.cm[ixa]*
%{_libdir}/ocaml/xmlrpc/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/xmlrpc
