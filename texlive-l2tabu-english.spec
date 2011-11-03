# revision 15878
# category Package
# catalog-ctan /info/l2tabu/english
# catalog-date 2008-03-16 17:19:11 +0100
# catalog-license gpl
# catalog-version 1.8.5.7
Name:		texlive-l2tabu-english
Version:	1.8.5.7
Release:	1
Summary:	English translation of "Obsolete packages and commands"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/english
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-english.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-english.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
English translation of the l2tabu practical guide to LaTeX2e by
Mark Trettin. A list of obsolete packages and commands.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu-english/l2tabuen.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu-english/l2tabuen.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
