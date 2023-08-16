%define git 20230816

Name:		kuserfeedback-qt6
Version:	1.2.1
Release:	%{?git:0.%{git}.}1
Summary:	Framework for collecting user feedback for applications via telemetry and surveys
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		https://invent.kde.org/libraries/kuserfeedback
%if 0%{!?git:1}
Source0:	https://download.kde.org/stable/kuserfeedback/kuserfeedback-%{version}.tar.xz
%else
Source0:	https://invent.kde.org/libraries/kuserfeedback/-/archive/master/kuserfeedback-master.tar.bz2#/kuserfeedback-%{git}.tar.bz2
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6ToolsTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Charts)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	bison
BuildRequires:	flex
Suggests:	kuserfeedback-translations = %{EVRD}

%description
Framework for collecting user feedback for applications via telemetry
and surveys.

# The translations are split out so they can be shared between the
# qt5 and qt6 versions of the package.
# This can be merged back into the main package once we drop KF5
%package -n kuserfeedback-translations
Summary:	Translations of kuserfeedback
Group:		Graphical desktop/KDE

%description -n kuserfeedback-translations
Translations of kuserfeedback

%files -n kuserfeedback-translations -f %{name}.lang

%files
%{_datadir}/qlogging-categories6/org_kde_UserFeedback.categories
%{_bindir}/userfeedbackctl
%{_libdir}/libKUserFeedbackCoreQt6.so*
%{_libdir}/libKUserFeedbackWidgetsQt6.so*
%{_qtdir}/qml/org/kde/userfeedback

%package console
Summary:	Application for viewing feedback collected by kuserfeedback
Group:		Development/KDE and Qt

%description console
Application for viewing feedback collected by kuserfeedback.

%files console
%{_bindir}/UserFeedbackConsole
%{_datadir}/applications/org.kde.kuserfeedback-console.desktop
%{_datadir}/metainfo/org.kde.kuserfeedback-console.appdata.xml

%package devel
Summary:	Development package for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} >= %{EVRD}

%description devel
Header files for development with %{name}.

%files devel
%{_includedir}/KUserFeedbackQt6/
%{_libdir}/cmake/KUserFeedbackQt6/
%{_qtdir}/mkspecs/modules/qt_KUserFeedbackCoreQt6.pri
%{_qtdir}/mkspecs/modules/qt_KUserFeedbackWidgetsQt6.pri
%optional %dir %{_datadir}/KDE
%optional %dir %{_datadir}/KDE/UserFeedbackConsole
%optional %{_datadir}/KDE/UserFeedbackConsole/*.qch

%prep
%autosetup -p1 -n kuserfeedback-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
D="$(pwd)"
%ninja_install -C build

cd %{buildroot}%{_datadir}/locale
for i in */LC_MESSAGES/*; do
	echo "%%lang($(echo $i |cut -d/ -f1)) %%{_datadir}/locale/$i" >>"$D"/%{name}.lang
done
