Summary:	library of python code used by various programs
Summary(pl):	Pliki wsadowe dla jêzyka python
Name:		pythonlib
Version:	1.22
Release:	4
Copyright:	GPL
Group:		Development/Libraries
Source:		%{name}-%{version}.tar.gz
Patch0:		pythonlib-Conf.patch 
Patch1:		pythonlib-user.patch 
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%description
This package contains code used by a variety of programs. It includes 
code for multifield listboxes and entry widgets with non-standard
keybindings, among others.

%description -l pl
W pakiecie znajduj± siê pliki wykorzystywane przez wiele programów.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1 

%build

%install
make install LIBDIR=$RPM_BUILD_ROOT%{_libdir}/rhs/python

gzip -9nf CHANGES

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz
%{_libdir}/rhs/python
