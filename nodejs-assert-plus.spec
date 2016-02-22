%{?scl:%scl_package nodejs-assert-plus}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-assert-plus
Version:        0.1.4
Release:        1.1%{?dist}
Summary:        Extra assertions on top of node's assert module
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          System Environment/Libraries
# MIT license text in README.md
License:        MIT
URL:            https://github.com/mcavage/node-assert-plus
Source0:        http://registry.npmjs.org/assert-plus/-/assert-plus-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This library is a super small wrapper over node's assert module that has two 
things: (1) the ability to disable assertions with the environment variable 
NODE_NDEBUG, and (2) some API wrappers for argument testing.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/assert-plus
cp -pr package.json assert.js %{buildroot}%{nodejs_sitelib}/assert-plus

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/assert-plus
%doc README.md

%changelog
* Wed Dec 11 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.4-1.1
- enable scl support

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-1
- new upstream release 0.1.4

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-2
- restrict to compatible arches

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-1
- initial package
