# Script generated with Bloom
pkgdesc="ROS - Library with C++ functions for SE(2/3) pose and 2D/3D point composition operations with uncertainty"
url='http://wiki.ros.org/pose_cov_ops'

pkgname='ros-kinetic-pose-cov-ops'
pkgver='0.2.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('mrpt'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-mrpt-bridge'
'ros-kinetic-roscpp'
)

depends=('mrpt'
'ros-kinetic-geometry-msgs'
'ros-kinetic-mrpt-bridge'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=pose_cov_ops
source=()
md5sums=()

prepare() {
    cp -R $startdir/pose_cov_ops $srcdir/pose_cov_ops
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

