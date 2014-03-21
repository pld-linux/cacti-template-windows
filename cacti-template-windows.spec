%define		template	windows
Summary:	Cacti WinXP-Win8, Win2000-Server 2012 x32/x64 Templates
Name:		cacti-template-%{template}
Version:	13
Release:	1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	Cacti_SNMP_Informant_Standard_Metrics_v%{version}.zip
# Source0-md5:	90f356a61f786cab266f4aea82fc3cf6
# https://github.com/mrlesmithjr/cacti/
URL:		http://forums.cacti.net/viewtopic.php?f=12&t=29832
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.554
BuildRequires:	unzip
Requires:	cacti >= 0.8.8a
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource

%description
SNMP Informant Standard Metrics for Windows Devices.

%prep
%setup -q -n Cacti_SNMP_Informant_Standard_Metrics_v%{version}

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
%cacti_import_template %{resourcedir}/cacti_host_template_windows_host_-_snmp_informant.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_cpu_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_disk_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_memory_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_network_statistics.xml
%{resourcedir}/cacti_data_query_snmp_informant_standard_-_objects_statistics.xml
%{resourcedir}/cacti_host_template_windows_host_-_snmp_informant.xml
%{resourcedir}/snmp_queries/snmp_informant_standard_cpu.xml
%{resourcedir}/snmp_queries/snmp_informant_standard_disk.xml
%{resourcedir}/snmp_queries/snmp_informant_standard_memory.xml
%{resourcedir}/snmp_queries/snmp_informant_standard_network.xml
%{resourcedir}/snmp_queries/snmp_informant_standard_objects.xml
