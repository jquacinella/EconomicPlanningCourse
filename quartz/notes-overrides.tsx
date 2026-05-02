// Quartz layout override that injects (a) a graph-ruled paper background and
// (b) an absolute-URL favicon link on every notes page. Lives at the top of
// the quartz/ directory (alongside quartz.config.ts and quartz.layout.ts) so
// it survives `bash setup.sh`, which protects this filename via the PROTECTED
// list.
//
// The favicon link is here (rather than relying on Quartz's default Head)
// because Quartz emits a *relative* href for the icon. On deep pages such as
// /notes/the_calculation_course/weeks/week-01-multivariable/reading-notes the
// relative href resolves to a non-existent path and the browser 404s the
// favicon on reload. An absolute URL bypasses that. Browsers honour the
// last-declared <link rel="icon">, so this body-rendered link wins over the
// default one in head.
//
// The SVG itself lives at quartz/static/notes-favicon.svg and is emitted by
// Plugin.Static under /notes/static/.

import { h, Fragment } from "preact"

const FAVICON_HREF =
  "https://jquacinella.github.io/EconomicPlanningCourse/notes/static/notes-favicon.svg"

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
  h(
    Fragment,
    null,
    h("style", { dangerouslySetInnerHTML: { __html: STYLES } }),
    h("link", { rel: "icon", type: "image/svg+xml", href: FAVICON_HREF }),
  )

export default function notesOverridesConstructor(_opts?: unknown) {
  return NotesOverrides
}
