import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import NotesOverrides from "./notes-overrides"

/**
 * Layout overrides for the Calculation Course notes section.
 *
 * The book proper is rendered by Quarto and lives at the root of the deployed
 * site. Quartz handles only the `/notes/` subtree. The header link back to the
 * book lives in `pageBody`. NotesOverrides injects a graph-ruled paper
 * background on every page (see notes-overrides.tsx).
 */
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [NotesOverrides()],
  footer: Component.Footer({
    links: {
      "Economic Planning Research Home": "https://jquacinella.github.io/EconomicPlanningCourse",
      "GitHub": "https://github.com/jquacinella/EconomicPlanningCourse",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [],
}
