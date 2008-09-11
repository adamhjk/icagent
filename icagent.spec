Name:           onehub-icagent
Version:        20af6b81641bd74ad0010415437688600f3ba9ff
Release:        1%{dist}
Summary:        A system tool to identify nodes to an iClassify server

Group:          Applications/Internet
License:        GPLv2
URL:            http://oss.hjksolutions.com/iclassify
Source:         http://github.com/onehub/icagent/tarball/{%version}/onehub-icagent-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
Requires: ruby >= 1.8.2

%description
icagent registers a node with iclassify, and lets you use small DSL for
classifiying them.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_datadir}/icagent/
%{__cp} -av bin/ %{buildroot}%{_bindir}
%{__cp} -av recipes/ lib/ %{buildroot}%{_datadir}/icagent/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/icagent/
%{_bindir}/icagent
%{_bindir}/icsearch
%{_bindir}/icwatcher

%changelog
* Tue Sep 11 2008 W. Andrew Loe III <loe@onehub.com> 0.1-1
- Initial RPM release
