%define		template	windows
Summary:	Cacti WinXP-Win8, Win2000-Server 2012 x32/x64 Templates
Name:		cacti-template-%{template}
Version:	14
Release:	1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	https://github.com/mrlesmithjr/cacti/archive/e2481cbb/%{template}-%{version}.tar.gz
# Source0-md5:	df37a4594527d53bb5070c9c21e8e709
URL:		http://forums.cacti.net/viewtopic.php?f=12&t=29832
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti >= 0.8.8b
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource

%description
SNMP Informant Standard Metrics for Windows Devices.

%prep
%setup -qc
mv cacti-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{resourcedir}
cp -a resource/* $RPM_BUILD_ROOT%{resourcedir}
cp -a template/* $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_data_query_snmp_informant_standard_-_cpu_statistics.xml
%cacti_import_template %{resourcedir}/cacti_data_query_snmp_informant_standard_-_disk_statistics.xml
%cacti_import_template %{resourcedir}/cacti_data_query_snmp_informant_standard_-_memory_statistics.xml
%cacti_import_template %{resourcedir}/cacti_data_query_snmp_informant_standard_-_network_statistics.xml
%cacti_import_template %{resourcedir}/cacti_data_query_snmp_informant_standard_-_objects_statistics.xml
%cacti_import_template %{resourcedir}/cacti_host_template_snmp_informant_windows.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_cpu_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_disk_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_memory_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_network_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_objects_statistics.xml
%{resourcedir}/cacti_host_template_snmp_informant_windows.xml
%{resourcedir}/snmp_queries/*.xml
