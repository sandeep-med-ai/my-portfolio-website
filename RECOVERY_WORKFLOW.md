# RECOVERY WORKFLOW

## CLEAN INSTALL WORKFLOW
1. Delete existing dependency artifacts:
   `Remove-Item -Recurse -Force node_modules, package-lock.json`
2. Reinstall from scratch:
   `npm install`

## DEPENDENCY RECOVERY WORKFLOW
If `npm run build` fails due to missing modules:
1. Run `npm install`
2. If issues persist, follow the **CLEAN INSTALL WORKFLOW**.

## BUILD RECOVERY WORKFLOW
If `astro build` fails:
1. Check terminal output for the exact file and line number (usually MDX syntax errors).
2. Validate `astro.config.mjs` for syntax errors.
3. Ensure no duplicate routes exist (e.g., `page.mdx` and `page.astro`).
4. Run `npm run build` again.

## ROLLBACK WORKFLOW
To revert to the last known stable state:
1. Identify the stable commit or state.
2. Run: `git reset --hard HEAD` (Note: This destroys uncommitted changes).
3. Clean the environment: `git clean -fd`

## DIST REGENERATION WORKFLOW
To ensure a clean production build:
1. Remove current build output:
   `Remove-Item -Recurse -Force dist`
2. Run build:
   `npm run build`

## NODE_MODULES RESET WORKFLOW
If the environment becomes corrupted:
1. Force remove the directory:
   `Remove-Item -Recurse -Force node_modules`
2. Reinstall:
   `npm install`
