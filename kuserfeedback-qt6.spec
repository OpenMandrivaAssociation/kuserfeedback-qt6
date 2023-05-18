Name:		kuserfeedback-qt6
Version:	1.2.0
Release:	1
Summary:	Framework for collecting user feedback for applications via telemetry and surveys
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		https://invent.kde.org/libraries/kuserfeedback
Source0:	https://download.kde.org/stable/kuserfeedback/kuserfeedback-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6ToolsTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Charts)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	bison
BuildRequires:	flex

%description
Framework for collecting user feedback for applications via telemetry
and surveys.

%files
%{_datadir}/qlogging-categories6/org_kde_UserFeedback.categories
%{_bindir}/userfeedbackctl
%{_datadir}/locale/*/LC_MESSAGES/userfeedbackprovider5_qt.qm
%{_libdir}/libKUserFeedbackCore.so*
%{_libdir}/libKUserFeedbackWidgets.so*
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
%dir %{_datadir}/KDE/UserFeedbackConsole
%{_datadir}/KDE/UserFeedbackConsole/*.qch
%{_datadir}/locale/*/LC_MESSAGES/userfeedbackconsole5_qt.qm

%package devel
Summary:	Development package for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} >= %{EVRD}

%description devel
Header files for development with %{name}.

%files devel
%{_includedir}/KUserFeedback/
%{_libdir}/libKUserFeedbackCore.so
%{_libdir}/libKUserFeedbackWidgets.so
%{_libdir}/cmake/KUserFeedback/
%{_qtdir}/mkspecs/modules/qt_KUserFeedbackCore.pri
%{_qtdir}/mkspecs/modules/qt_KUserFeedbackWidgets.pri

%prep
%autosetup -p1 -n kuserfeedback-%{version}
%cmake \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
