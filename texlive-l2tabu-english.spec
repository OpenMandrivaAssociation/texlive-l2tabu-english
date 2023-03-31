Name:		texlive-l2tabu-english
Version:	15878
Release:	2
Summary:	English translation of "Obsolete packages and commands"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/english
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-english.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-english.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
English translation of the l2tabu practical guide to LaTeX2e by
Mark Trettin. A list of obsolete packages and commands.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu-english/l2tabuen.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu-english/l2tabuen.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
