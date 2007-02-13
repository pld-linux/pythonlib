Summary:	Library of Python code used by various programs
Summary(pl.UTF-8):	Pliki wsadowe dla języka Python
Summary(pt_BR.UTF-8):	Biblioteca de código Python usada por vários programas Red Hat
Summary(es.UTF-8):	Biblioteca de código Python usada por varios programas Red Hat
Name:		pythonlib
Version:	1.26
Release:	4
License:	GPL
Group:		Development/Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	986dfa39d68a33e428b6803f953080fc
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains code used by a variety of programs. It includes
code for multifield listboxes and entry widgets with non-standard
keybindings, among others.

%description -l pl.UTF-8
W pakiecie znajdują się pliki wykorzystywane przez wiele programów.

%description -l pt_BR.UTF-8
Este pacote contém o código usado por uma variedade de programas Red
Hat. Inclui código para caixas de listas multicampo e widgets de
entrada de dados com associações de teclas não padrão, entre outros.

%description -l es.UTF-8
Este paquete contiene el código usado por una variedad de programas
Red Hat. Incluye código para cajas de listas multicampo y widgets de
entrada de datos con asociaciones de teclas no padrón, entre otros.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install LIBDIR=$RPM_BUILD_ROOT%{_libdir}/python


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{_libdir}/python
