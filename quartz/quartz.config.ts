import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz configuration for the multi-course notes section.
 *
 * The notes site is published as a sub-section of the main site at `/notes/`.
 * Content is organized by course under quartz/content/:
 *   content/the_calculation_course/ -> courses/the_calculation_course/notes/
 *   content/201/                    -> courses/201/notes/
 *   content/the_crypto_course/      -> courses/the_crypto_course/notes/
 *
 * Resulting URLs:
 *   /notes/the_calculation_course/weeks/...
 *   /notes/201/weeks/...
 *   /notes/the_crypto_course/weeks/...
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Heterodox Econ Courses — Notes",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "jquacinella.github.io/EconomicPlanningCourse/notes",
    ignorePatterns: [
      "private",
      "templates",
      // Obsidian vault config dirs (one per course vault)
      "the_calculation_course/.obsidian",
      "201/.obsidian",
      "the_crypto_course/.obsidian",
      // Don't serve raw PDF attachments
      "the_calculation_course/attachments/**/*.pdf",
      "201/attachments/**/*.pdf",
      "the_crypto_course/attachments/**/*.pdf",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "git", "filesystem"] }),
      Plugin.SyntaxHighlighting({ theme: { light: "github-light", dark: "github-dark" }, keepBackground: false }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
