%define		plugin		ldapsearch
Summary:	Dokuwiki plugin to search LDAP directories for values
Name:		dokuwiki-plugin-%{plugin}
Version:	20090601
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://freecode.baselineit.net/dokuwiki/ldapsearch-latest.zip
# Source0-md5:	9822e7d7a6dae69534ac645444c4258d
Patch0:		pass-by-reference.patch
URL:		http://www.dokuwiki.org/plugin:ldapsearch
BuildRequires:	rpmbuild(macros) >= 1.520
BuildRequires:	unzip
Requires:	dokuwiki >= 20061106
Requires:	php-ldap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin allows you to search LDAP directories for values (like
telephone numbers) from within your page.

%prep
%setup -qc
mv %{plugin}/* .
%patch -P0 -p1

version=$(awk -F"'" '/date/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/conf
