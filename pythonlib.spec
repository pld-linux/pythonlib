Summary:     library of python code used by various programs
Summary(pl): Pliki wsadowe dla jêzyka python
Name:        pythonlib
Version:     1.22
Release:     3
Copyright:   GPL
Group:       Development/Libraries
Source:      %{name}-%{version}.tar.gz
Patch0:      pythonlib-Conf.patch 
Patch1:      pythonlib-user.patch 
Requires:    python
Buildarch:   noarch
BuildRoot:   /tmp/%{name}-%{version}-root

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
make install LIBDIR=$RPM_BUILD_ROOT/usr/lib/rhs/python

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc CHANGES
/usr/lib/rhs/python

%changelog
* Sun Nov 15 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.22-3]
- build for Linux PLD, from non root account,
- added pl translation,
- major changes.

* Fri Jul 10 1998 Michael Maher <mike@redhat.com> 
- patched Conf.py so that kernelcfg works.
- added Buildroot.

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
Added some stuff to deal with -k

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
do not require tkinter; apps that explicitly use tkinter through
pythonlib should require tkinter themselves.

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
require tkinter

* Fri Oct 31 1997 Michael K. Johnson <johnsonm@redhat.com>
ConfFstab for cabaret

* Mon Sep 29 1997 Michael K. Johnson <johnsonm@redhat.com>
Major changes for new version of netcfg.
- Clone files keep differences in some way appropriate to the type of file.
- RCS management of almost all files (all but password-type files) -- just
  create a subdirectory called RCS in any directory where you want to
  monitor changes made by control-panel tools that use pythonlib.  That
  can also be a symlink, but watch for filename conflicts.
- Smart chatfile handling that knows something about the contents of a
  chatfile.
- Far better algorithm for finding free user and group ids: first do the
  old sparse search, then if that fails, search for first free id.  This
  algorithm is used for both user and group ids.
- EntryBox class is a toplevel that provides a single entry in a modal manner.

Also made it a noarch package.

* Mon Aug 11 1997 Michael K. Johnson <johnsonm@redhat.com>
Added fix for shadow files.  (Not a CVS branch; change made in master as well)

* Mon Jun 02 1997 Michael K. Johnson <johnsonm@redhat.com>
Added proper error raising and error-on-missing files for kernelcfg.

* Mon Apr 21 1997 Michael K. Johnson <johnsonm@redhat.com>
Fields terminated only by separator or end of line.

* Fri Mar 28 1997 Michael K. Johnson <johnsonm@redhat.com>
Fixed quoted ampersand in ConfShellVar

* Wed Mar 12 1997 Michael K. Johnson <johnsonm@redhat.com>
Fixed quoted equals in ConfShellVar

* Wed Mar 05 1997 Michael K. Johnson <johnsonm@redhat.com>
Changed to /etc/ppp/pap-secrets

* Wed Feb 26 1997 Michael K. Johnson <johnsonm@redhat.com>
Added class for managing /etc/pap-secrets.
Improved class for managing /etc/sysconfig/static-routes
