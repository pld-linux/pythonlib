Summary:	library of python code used by various programs
Summary(pl):	Pliki wsadowe dla jêzyka python
Summary(pt_BR):	Biblioteca de código python usada por vários programas Red Hat
Summary(es):	Biblioteca de código python usada por varios programas Red Hat
Name:		pythonlib
Version:	1.26
Release:	3
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Source0:	%{name}-%{version}.tar.gz
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%description
This package contains code used by a variety of programs. It includes
code for multifield listboxes and entry widgets with non-standard
keybindings, among others.

%description -l pl
W pakiecie znajduj± siê pliki wykorzystywane przez wiele programów.

%description -l pt_BR
Este pacote contém o código usado por uma variedade de programas
Red Hat.  Inclui código para caixas de listas multicampo e widgets de
entrada de dados com associações de teclas não padrão, entre outros.

%description -l es
Este paquete contiene el código usado por una variedad de programas
Red Hat.  Incluye código para cajas de listas multicampo y widgets de
entrada de datos con asociaciones de teclas no padrón, entre otros.

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
%doc *.gz
%{_libdir}/python
