%define prj    Horde_SQL

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-sql
Version:       0.0.2
Release:       4
Summary:       SQL Utility Class
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
Horde_SQL:: contains some utility functions for dealing with SQL.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/SQL
%{peardir}/Horde/SQL.php
%{peardir}/Horde/SQL/Attributes.php
%{peardir}/Horde/SQL/Keywords.php




%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 564101
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 524855
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel ver to 2

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 509401
- removed BuildRequires: horde-framework
- import horde-sql


* Tue Mar  3 2009 Richard Bos <rbos@opensuse.org> - 0.0.2
- Change dependency to horde-framework from just horde
* Tue Dec 23 2008 Richard Bos <rbos@opensuse.org> - 0.0.2
- Changed the pear install command, use package.xml instead of the tarbal
* Wed Nov 26 2008 Richard Bos <rbos@opensuse.org> - 0.0.2
- initial version
