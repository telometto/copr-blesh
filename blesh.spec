# globs
%global build_branch master
%global pkg_name ble.sh

%global build_repo https://github.com/akinomyoga/ble.sh


# Spec file Preamble
Name:    %{package_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: Copr repo of akinomyoga's bash editor "ble.sh"	

License: BSD-3-Clause license
URL:     %{build_repo}
Source0: https://github.com/akinomyoga/ble.sh.git

BuildRequires: git
BuildRequires: make
BuildRequires: gawk

# What this package does.
%description
Bash Line Editor―a full-featured line editor written in pure Bash! Syntax highlighting, auto suggestions, vim modes, etc. are available in Bash interactive sessions!


# These are instructions to prepare sources for the build.
%prep
%setup -q

# These are instructions to build the package.
%build
# Nothing to do.

# This installs package into system after it has been been built.
# Invoked e.g. by `dnf install example`.
%install
make -C ble.sh install PREFIX=~/.local
echo 'source ~/.local/share/blesh/ble.sh' >> ~/.bashrc

# Here you should list all the files the package provides.
%files
%doc

# What has changed since the last version. High level overview
# over the last commits.
%changelog
* Mon May 9 2022 telometto <telometto@protonmail.com> 1.0.0-1
- Initial version
