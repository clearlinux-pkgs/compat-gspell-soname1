#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-gspell-soname1
Version  : 1.6.1
Release  : 16
URL      : https://download.gnome.org/sources/gspell/1.6/gspell-1.6.1.tar.xz
Source0  : https://download.gnome.org/sources/gspell/1.6/gspell-1.6.1.tar.xz
Summary  : Spell checking for GTK+
Group    : Development/Tools
License  : LGPL-2.1
Requires: compat-gspell-soname1-lib = %{version}-%{release}
Requires: compat-gspell-soname1-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libc6-locale
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : valgrind
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
gspell - a spell-checking library for GTK+ applications
=======================================================

%package lib
Summary: lib components for the compat-gspell-soname1 package.
Group: Libraries
Requires: compat-gspell-soname1-license = %{version}-%{release}

%description lib
lib components for the compat-gspell-soname1 package.


%package license
Summary: license components for the compat-gspell-soname1 package.
Group: Default

%description license
license components for the compat-gspell-soname1 package.


%prep
%setup -q -n gspell-1.6.1
cd %{_builddir}/gspell-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586223589
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1586223589
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-gspell-soname1
cp %{_builddir}/gspell-1.6.1/COPYING %{buildroot}/usr/share/package-licenses/compat-gspell-soname1/5013d109e2fe11116d2b062bb46114a398276501
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/gspell-app1
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-checker-dialog.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-checker.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-entry-buffer.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-entry.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-enum-types.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-language-chooser-button.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-language-chooser-dialog.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-language-chooser.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-language.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-navigator-text-view.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-navigator.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-text-buffer.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-text-view.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell-version.h
rm -f %{buildroot}/usr/include/gspell-1/gspell/gspell.h
rm -f %{buildroot}/usr/lib64/girepository-1.0/Gspell-1.typelib
rm -f %{buildroot}/usr/lib64/libgspell-1.so
rm -f %{buildroot}/usr/lib64/pkgconfig/gspell-1.pc
rm -f %{buildroot}/usr/share/gir-1.0/Gspell-1.gir
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellChecker.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellCheckerDialog.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellEntry.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellEntryBuffer.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellLanguage.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellLanguageChooser.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellLanguageChooserButton.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellLanguageChooserDialog.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellNavigator.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellNavigatorTextView.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellTextBuffer.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GspellTextView.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GtkEntry-support.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/GtkTextView-support.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/annexes.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/annotation-glossary.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/api-index-full.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/api-reference.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/core-classes.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/gspell-1.0.devhelp2
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/home.png
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/index.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/intro.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/language-choosers.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/left-insensitive.png
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/left.png
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/object-tree.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/right-insensitive.png
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/right.png
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/spell-checker-dialog.html
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/style.css
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/up-insensitive.png
rm -f %{buildroot}/usr/share/gtk-doc/html/gspell-1.0/up.png
rm -f %{buildroot}/usr/share/vala/vapi/gspell-1.deps
rm -f %{buildroot}/usr/share/vala/vapi/gspell-1.vapi
## install_append content
rm -rf %{buildroot}/usr/share/locale
## install_append end

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgspell-1.so.1
/usr/lib64/libgspell-1.so.1.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-gspell-soname1/5013d109e2fe11116d2b062bb46114a398276501
