from conans import ConanFile, CMake, tools


class DemoAppConan(ConanFile):
    name = "demo-app"
    version = "1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of DemoApp here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    generators = "cmake"

    exports_sources = "src/CMakeLists.txt", "src/main.cpp"

    def requirements(self):
        self.requires("serviceA/1.0")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        pass
#         self.run("git clone https://github.com/conan-io/hello.git")
#         # This small hack might be useful to guarantee proper /MT /MD linkage
#         # in MSVC if the packaged project doesn't have variables to set it
#         # properly
#         tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(HelloWorld)",
#                               '''PROJECT(HelloWorld)
# include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.exe", dst="bin", keep_path=False)

    def package_info(self):
        pass

