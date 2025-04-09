import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import postcss from 'rollup-plugin-postcss'

// https://vitejs.dev/config/
export default defineConfig(({mode}) => {
  //This is needed so the postCss plugin will only run on build
  const postCss = mode === 'production' ? postcss({
    extract: 'static/css/main.css',
    minimize: false,
    sourceMap: true,
  }) : null;

  return {
    plugins: [react(), postCss],
    resolve: {
      mainFields: [],
    },
    build: {
      manifest: true,
      outDir: 'build',
      sourcemap: true,
      rollupOptions: {
        output: {
          assetFileNames: (assetInfo) => {
            console.log(assetInfo)
            let extType = assetInfo.name.split('.').at(1);
            if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(extType)) {
              extType = 'img';
            }
            return `static/${extType}/main.[hash][extname]`;
          },
          entryFileNames: 'static/js/main.[hash].js',
          format: 'umd'
        },
      },
    },
    esbuild: {
      loader: 'tsx',
      include: /src\/.*\.tsx?$/,
      exclude: [],
    },

    optimizeDeps: {
      esbuildOptions: {
        loader: {
          '.ts': 'tsx',
        },
      },
    },
  }
})
