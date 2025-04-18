#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v24
# autospec commit: a88ffdc
#
Name     : texmaker
Version  : 6.0.0
Release  : 24
URL      : https://www.xm1math.net/texmaker/texmaker-6.0.0.tar.bz2
Source0  : https://www.xm1math.net/texmaker/texmaker-6.0.0.tar.bz2
Summary  : LaTeX editor
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 GPL-2.0+ LGPL-2.0
Requires: texmaker-bin = %{version}-%{release}
Requires: texmaker-data = %{version}-%{release}
Requires: texmaker-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Texmaker is a clean, highly configurable LaTeX editor with good hot key 
 support and extensive LaTeX documentation. Texmaker integrates many tools 
 needed to develop documents with LaTeX, in just one application.

%package bin
Summary: bin components for the texmaker package.
Group: Binaries
Requires: texmaker-data = %{version}-%{release}
Requires: texmaker-license = %{version}-%{release}

%description bin
bin components for the texmaker package.


%package data
Summary: data components for the texmaker package.
Group: Data

%description data
data components for the texmaker package.


%package license
Summary: license components for the texmaker package.
Group: Default

%description license
license components for the texmaker package.


%prep
%setup -q -n texmaker-6.0.0
cd %{_builddir}/texmaker-6.0.0

%build
## build_prepend content
PATH="/usr/lib64/qt6/bin:$PATH"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744138078
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744138078
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/texmaker
cp %{_builddir}/texmaker-%{version}/3rdparty/pdfium/LICENSE %{buildroot}/usr/share/package-licenses/texmaker/689c532308da601d10beba61b6672b0c16dc3b48 || :
cp %{_builddir}/texmaker-%{version}/3rdparty/pdfium/third_party/pymock/LICENSE.txt %{buildroot}/usr/share/package-licenses/texmaker/794a893e510ca5c15c9c97a609ce47b0df74fc1a || :
cp %{_builddir}/texmaker-%{version}/COPYING %{buildroot}/usr/share/package-licenses/texmaker/2d29c273fda30310211bbf6a24127d589be09b6c || :
cp %{_builddir}/texmaker-%{version}/datas/license.txt %{buildroot}/usr/share/package-licenses/texmaker/0b0249b0fdc22a55c9ebb98ce74ae136487e4679 || :
cp %{_builddir}/texmaker-%{version}/datas/license_html.txt %{buildroot}/usr/share/package-licenses/texmaker/14b52b17238af3275260353bcbde8b4d950db8e6 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/texmaker

%files data
%defattr(-,root,root,-)
/usr/share/applications/texmaker.desktop
/usr/share/metainfo/texmaker.metainfo.xml
/usr/share/pixmaps/texmaker.png
/usr/share/texmaker/AUTHORS
/usr/share/texmaker/CHANGELOG.txt
/usr/share/texmaker/COPYING
/usr/share/texmaker/README_DIC_fr_FR.txt
/usr/share/texmaker/README_cs_CZ.txt
/usr/share/texmaker/README_de_DE_frami.txt
/usr/share/texmaker/README_en_US.txt
/usr/share/texmaker/README_es_ES.txt
/usr/share/texmaker/README_hu_HU.txt
/usr/share/texmaker/README_pl.txt
/usr/share/texmaker/README_pt_PT.txt
/usr/share/texmaker/ca_CA.aff
/usr/share/texmaker/ca_CA.dic
/usr/share/texmaker/cs_CZ.aff
/usr/share/texmaker/cs_CZ.dic
/usr/share/texmaker/de_DE.aff
/usr/share/texmaker/de_DE.dic
/usr/share/texmaker/doc1.png
/usr/share/texmaker/doc10.png
/usr/share/texmaker/doc11.png
/usr/share/texmaker/doc12.png
/usr/share/texmaker/doc13.png
/usr/share/texmaker/doc14.png
/usr/share/texmaker/doc15.png
/usr/share/texmaker/doc16.png
/usr/share/texmaker/doc17.png
/usr/share/texmaker/doc2.png
/usr/share/texmaker/doc20.png
/usr/share/texmaker/doc21.png
/usr/share/texmaker/doc22.png
/usr/share/texmaker/doc3.png
/usr/share/texmaker/doc4.png
/usr/share/texmaker/doc5.png
/usr/share/texmaker/doc6.png
/usr/share/texmaker/doc6bis.png
/usr/share/texmaker/doc7.png
/usr/share/texmaker/doc8.png
/usr/share/texmaker/doc9.png
/usr/share/texmaker/en_GB.aff
/usr/share/texmaker/en_GB.dic
/usr/share/texmaker/en_US.aff
/usr/share/texmaker/en_US.dic
/usr/share/texmaker/es_ES.aff
/usr/share/texmaker/es_ES.dic
/usr/share/texmaker/fr_FR.aff
/usr/share/texmaker/fr_FR.dic
/usr/share/texmaker/hardwordwrap_selection_80col.tms
/usr/share/texmaker/hu_HU.aff
/usr/share/texmaker/hu_HU.dic
/usr/share/texmaker/it_IT.aff
/usr/share/texmaker/it_IT.dic
/usr/share/texmaker/it_IT_README.txt
/usr/share/texmaker/latexhelp.html
/usr/share/texmaker/nl_NL.aff
/usr/share/texmaker/nl_NL.dic
/usr/share/texmaker/pl_PL.aff
/usr/share/texmaker/pl_PL.dic
/usr/share/texmaker/pt_PT.aff
/usr/share/texmaker/pt_PT.dic
/usr/share/texmaker/qt_ar.qm
/usr/share/texmaker/qt_ca.qm
/usr/share/texmaker/qt_cs.qm
/usr/share/texmaker/qt_da.qm
/usr/share/texmaker/qt_de.qm
/usr/share/texmaker/qt_en.qm
/usr/share/texmaker/qt_es.qm
/usr/share/texmaker/qt_fa.qm
/usr/share/texmaker/qt_fi.qm
/usr/share/texmaker/qt_fr.qm
/usr/share/texmaker/qt_gl.qm
/usr/share/texmaker/qt_he.qm
/usr/share/texmaker/qt_hu.qm
/usr/share/texmaker/qt_it.qm
/usr/share/texmaker/qt_ja.qm
/usr/share/texmaker/qt_ko.qm
/usr/share/texmaker/qt_lt.qm
/usr/share/texmaker/qt_pl.qm
/usr/share/texmaker/qt_pt.qm
/usr/share/texmaker/qt_ru.qm
/usr/share/texmaker/qt_sk.qm
/usr/share/texmaker/qt_sl.qm
/usr/share/texmaker/qt_sv.qm
/usr/share/texmaker/qt_uk.qm
/usr/share/texmaker/qt_zh_CN.qm
/usr/share/texmaker/qt_zh_TW.qm
/usr/share/texmaker/texmaker.svg
/usr/share/texmaker/texmaker128x128.png
/usr/share/texmaker/texmaker16x16.png
/usr/share/texmaker/texmaker22x22.png
/usr/share/texmaker/texmaker32x32.png
/usr/share/texmaker/texmaker48x48.png
/usr/share/texmaker/texmaker64x64.png
/usr/share/texmaker/texmaker_ar.qm
/usr/share/texmaker/texmaker_cs.qm
/usr/share/texmaker/texmaker_de.qm
/usr/share/texmaker/texmaker_el.qm
/usr/share/texmaker/texmaker_es.qm
/usr/share/texmaker/texmaker_fa.qm
/usr/share/texmaker/texmaker_fr.qm
/usr/share/texmaker/texmaker_gl.qm
/usr/share/texmaker/texmaker_hu.qm
/usr/share/texmaker/texmaker_it.qm
/usr/share/texmaker/texmaker_lv.qm
/usr/share/texmaker/texmaker_nl.qm
/usr/share/texmaker/texmaker_pl.qm
/usr/share/texmaker/texmaker_pt.qm
/usr/share/texmaker/texmaker_pt_BR.qm
/usr/share/texmaker/texmaker_ru.qm
/usr/share/texmaker/texmaker_se.qm
/usr/share/texmaker/texmaker_sr.qm
/usr/share/texmaker/texmaker_uk.qm
/usr/share/texmaker/texmaker_vi_VN.qm
/usr/share/texmaker/texmaker_zh_CN.qm
/usr/share/texmaker/texmaker_zh_TW.qm
/usr/share/texmaker/titlecase_selection.tms
/usr/share/texmaker/usermanual_en.html
/usr/share/texmaker/usermanual_fr.html

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/texmaker/0b0249b0fdc22a55c9ebb98ce74ae136487e4679
/usr/share/package-licenses/texmaker/14b52b17238af3275260353bcbde8b4d950db8e6
/usr/share/package-licenses/texmaker/2d29c273fda30310211bbf6a24127d589be09b6c
/usr/share/package-licenses/texmaker/689c532308da601d10beba61b6672b0c16dc3b48
/usr/share/package-licenses/texmaker/794a893e510ca5c15c9c97a609ce47b0df74fc1a
