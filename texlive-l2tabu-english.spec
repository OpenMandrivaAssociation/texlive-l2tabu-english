# revision 15878
# category Package
# catalog-ctan /info/l2tabu/english
# catalog-date 2008-03-16 17:19:11 +0100
# catalog-license gpl
# catalog-version 1.8.5.7
Name:		texlive-l2tabu-english
Version:	1.8.5.7
Release:	10
Summary:	English translation of "Obsolete packages and commands"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/english
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-english.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-english.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.8.5.7-2
+ Revision: 753063
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.8.5.7-1
+ Revision: 718791
- texlive-l2tabu-english
- texlive-l2tabu-english
- texlive-l2tabu-english
- texlive-l2tabu-english

