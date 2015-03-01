module.exports = function(grunt) {
    grunt.initConfig({
        config: {
            js_files: ["static/**/*.js", '!static/build/**/*.js'],
            css_files: ["static/**/*.css", "static/**/*.styl", '!static/build/**/*.css']
        },
        uglify: {
            dist: {
                options: {
                    mangle: {
                        toplevel: true
                    }
                },
                files: {
                    'static/build/app.min.js': ['<%= config.js_files %>']
                }
            },
            dev: {
                files: {
                    'static/build/app.min.js': [' <%= config.js_files %>']
                }
            }
        },
        stylus: {
            compile: {
                options: {
                    compress: false
                },
                files: {
                    'static/build/app.min.css': ['<%= config.css_files %>']
                }

            }
        },
        clean: {
            build: ['static/build/']
        },
        watch: {
            grunt: {
                files: ['Gruntfile.js']
            },
            js: {
                files: ['<%= config.js_files %>'],
                tasks: ['uglify:dev']
            },
            css: {
                files: ['<%= config.css_files %>'],
                tasks: ['stylus:compile']
            }
        },
        bower_concat: {
            all: {
                dest: 'static/build/_bower.js',
                cssDest: 'static/build/_bower.css',
                dependencies: {
                    'underscore': 'jquery',
                    'backbone': 'underscore'
                },
                bowerOptions: {
                    relative: false
                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.registerTask('build', ['clean', 'uglify', 'stylus'])
    grunt.loadNpmTasks('grunt-bower-concat');
};
