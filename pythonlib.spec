Summary:	library of python code used by various programs
Summary(pl):	Pliki wsadowe dla jЙzyka python
Name:		pythonlib
Version:	1.26
Release:	2
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Source0:	%{name}-%{version}.tar.gz
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%description
This package contains code used by a variety of programs. It includes
code for multifield listboxes and entry widgets with non-standard
keybindings, among others.

%description -l pl
W pakiecie znajduj╠ siЙ pliki wykorzystywane przez wiele programСw.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install LIBDIR=$RPM_BUILD_ROOT%{_libdir}/python

gzip -9nf CHANGES

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz
%{_libdir}/python
