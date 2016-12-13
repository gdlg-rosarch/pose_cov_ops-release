Name:           ros-jade-pose-cov-ops
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS pose_cov_ops package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/pose_cov_ops
Source0:        %{name}-%{version}.tar.gz

Requires:       mrpt-devel
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-mrpt-bridge
Requires:       ros-jade-roscpp
BuildRequires:  mrpt-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-mrpt-bridge
BuildRequires:  ros-jade-roscpp

%description
Library with C++ functions for SE(2/3) pose and 2D/3D point composition
operations with uncertainty

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Dec 13 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.5-0
- Autogenerated by Bloom

