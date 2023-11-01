Name:           pcm
Version:        202211
Release:        3%{?dist}
Summary:        Intel(r) Performance Counter Monitor
License:        BSD
Url:            https://github.com/intel/pcm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
ExclusiveArch:  %{ix86} x86_64

%description

Intel(r) Performance Counter Monitor (Intel(r) PCM) is an application
programming interface (API) and a set of tools based on the API to
monitor performance and energy metrics of Intel(r) Core(tm), Xeon(r),
Atom(tm) and Xeon Phi(tm) processors. PCM works on Linux, Windows,
Mac OS X, FreeBSD and DragonFlyBSD operating systems.

%prep
%autosetup

%build
%set_build_flags
%cmake -DCMAKE_BUILD_TYPE=CUSTOM 
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/usr/share/doc/PCM/*.md
rm -rf %{buildroot}/usr/share/doc/PCM/*.txt

%files
%license LICENSE
%doc doc/LINUX_HOWTO.txt README.md doc/FAQ.md doc/CUSTOM-COMPILE-OPTIONS.md doc/ENVVAR_README.md doc/PCM-EXPORTER.md doc/PCM-SENSOR-SERVER-README.md doc/PCM_RAW_README.md doc/DOCKER_README.md doc/license.txt
%{_sbindir}/%{name}-core
%{_sbindir}/%{name}-iio
%{_sbindir}/%{name}-latency
%{_sbindir}/%{name}-lspci
%{_sbindir}/%{name}-memory
%{_sbindir}/%{name}-msr
%{_sbindir}/%{name}-mmio
%{_sbindir}/%{name}-numa
%{_sbindir}/%{name}-accel
%{_sbindir}/%{name}-pcicfg
%{_sbindir}/%{name}-pcie
%{_sbindir}/%{name}-power
%{_sbindir}/%{name}-sensor
%{_sbindir}/%{name}-sensor-server
%{_sbindir}/%{name}-tsx
%{_sbindir}/%{name}-raw
%{_sbindir}/%{name}
%{_bindir}/%{name}-client
%{_sbindir}/%{name}-daemon
%{_sbindir}/%{name}-bw-histogram
%{_datadir}/%{name}/

%changelog
* Thu Nov 24 2022 Roman Dementiev <roman.dementiev@intel.com> 0.1-10
- Update to new upstream repository location and the name
- Update to version 202211

* Tue Jul 26 2022 Roman Dementiev <roman.dementiev@intel.com> 0.1-9
- Update to version 202207

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 202205-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 202112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jul 26 2021 Roman Dementiev <roman.dementiev@intel.com> 0.1-8
- Update to version 202107
- Add pcm-mmio utility to rpm spec

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 202105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Roman Dementiev <roman.dementiev@intel.com> 0.1-7
- Implement suggestions from Fedora review.

* Fri Mar 26 2021 William Cohen <wcohen@redhat.com> 0.1-6
- Clean up pcm.spec.

* Tue Aug 25 2020 Roman Dementiev <roman.dementiev@intel.com> 0.1-5
- Add pcm-raw under %files

* Wed Apr 01 2020 Otto Bruggeman <otto.g.bruggeman@intel.com> 0.1-4
- Add pcm-sensor-server under %files

* Mon Nov 25 2019 Roman Dementiev <roman.dementiev@intel.com> 0.1-3
- call make install and use %{_sbindir} or %{_bindir}

* Mon Oct 21 2019 Roman Dementiev <roman.dementiev@intel.com> 0.1-2
- add opCode file to /usr/share/pcm
- use "install" to copy pcm-bw-histogram.sh

* Fri Oct 18 2019 Roman Dementiev <roman.dementiev@intel.com> 0.1-1
- created spec file

