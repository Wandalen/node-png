{
  "targets":
  [{
      "target_name": "png",
      "sources":
      [
        "src/common.cpp",
        "src/png_encoder.cpp",
        "src/png.cpp",
        "src/fixed_png_stack.cpp",
        "src/dynamic_png_stack.cpp",
        "src/module.cpp",
        "src/buffer_compat.cpp",
      ],

#      'msvs_settings':
#      {
#        'VCCLCompilerTool':
#        {
#          'RuntimeLibrary': 2, # multi threaded DLL
#        },
#      },

      "conditions" :
      [
        [
          'OS=="linux"', {
            "libraries" : [
              '-lpng',
              '-lz'
            ],
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ]
          }
        ],
        [
          'OS=="mac"', {
            'xcode_settings': {
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
            },
            "libraries" : [
              '<!@(pkg-config libpng --libs)'
            ]
          }
        ],
        [
          'OS=="win"', {
            "include_dirs" : [ "gyp/include" ],
          }
        ],
        [
          'OS=="win" and target_arch=="ia32old"', {
            "libraries" : [
              '<(module_root_dir)/gyp/lib/png12.lib',
              '<(module_root_dir)/gyp/lib/zlib.lib'
            ]
          }
        ],
        [
          'OS=="win" and target_arch=="ia32"', {
            "libraries" : [
              '<(module_root_dir)/gyp/lib-32MT/zlibstatic.lib',
              '<(module_root_dir)/gyp/lib-32MT/libpng12_static.lib'
            ]
          }
        ],
        [
          'OS=="win" and target_arch=="x64"', {
            "libraries" : [
              '<(module_root_dir)/gyp/lib-64MT/zlibstatic.lib',
              '<(module_root_dir)/gyp/lib-64MT/libpng12_static.lib'
            ]
          }
        ]

      ]
  }]
}