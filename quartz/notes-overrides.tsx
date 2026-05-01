// Quartz layout override that injects a graph-ruled paper background on every
// notes page. Lives at the top of the quartz/ directory (alongside
// quartz.config.ts and quartz.layout.ts) so it survives `bash setup.sh`,
// which protects this filename via the PROTECTED list.
//
// The component renders a single <style> element. The CSS uses CSS variables
// so the grid line color shifts between light and dark mode. The grid pattern
// is fixed-attachment so it doesn't scroll with content.

import { h } from "preact"

const STYLES = `
:root {
  --graph-line: rgba(40, 75, 99, 0.07);
}
:root[saved-theme="dark"] {
  --graph-line: rgba(255, 255, 255, 0.04);
}
body {
  background-image:
    linear-gradient(to right, var(--graph-line) 1px, transparent 1px),
    linear-gradient(to bottom, var(--graph-line) 1px, transparent 1px);
  background-size: 24px 24px;
  background-attachment: fixed;
}
`.trim()

// Quartz components are functions returning JSX. Constructors return that
// function. We don't import QuartzComponentConstructor because the upstream
// type definition only exists after `bash setup.sh` runs — keeping this file
// type-safe without a build-time dependency on the upstream tree.
const NotesOverrides = () =>
  h("style", { dangerouslySetInnerHTML: { __html: STYLES } })

export default function notesOverridesConstructor(_opts?: unknown) {
  return NotesOverrides
}
