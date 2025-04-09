import { defineConfig, mergeConfig } from 'vitest/config'

export default defineConfig({
    test: {
        globals: true,
        environment: 'happy-dom',
        setupFiles: './src/tests/setup.ts'
    },
})
