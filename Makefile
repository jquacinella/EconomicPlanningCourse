# Makefile for the Heterodox Econ Courses + Research monorepo.
#
# Day-to-day editing (live reload):
#   make dev / dev-calc      — Calculation Course at http://localhost:4444
#   make dev-marxian         — Marxian Formalization research project at http://localhost:4445
#   make dev-postcap         — Postcapitalism After AI research track at http://localhost:4446
#   make dev-notes           — Quartz notes site at http://localhost:8080
#
# Full-site build (one-shot, for checking before push):
#   make build          — build all courses + research projects + notes into _site/
#   make preview        — build then serve _site/ at http://localhost:$(PORT) (default 9200)
#   make build-calc     — build only the Calculation Course
#   make build-notes    — build only the Quartz notes site
#   make clean          — remove _site/ and all _book/ dirs
#
# Prerequisites: quarto, uv, node/npm (with Quartz set up via quartz/setup.sh)

# Each entry is path:slug — path is relative to repo root, slug is the URL segment under /courses/ or /research/.
COURSES    := courses/the_calculation_course
RESEARCH   := research/marxian_formalization research/postcapitalism_after_ai
ALL_BOOKS  := $(COURSES) $(RESEARCH)
SITE       := _site
PORT       := 9200

.PHONY: build preview dev dev-calc dev-marxian dev-postcap dev-notes build-calc build-notes sync-quartz-static stitch clean help

## dev-calc: Live-reload quarto preview for the Calculation Course (port 4444)
dev-calc:
	@echo "Starting quarto preview for the_calculation_course at http://localhost:4444"
	cd courses/the_calculation_course && uv run quarto preview

## dev-marxian: Live-reload quarto preview for the Marxian Formalization research project (port 4445)
dev-marxian:
	@echo "Starting quarto preview for marxian_formalization at http://localhost:4445"
	cd research/marxian_formalization && uv run quarto preview

## dev-postcap: Live-reload quarto preview for the Postcapitalism After AI research track (port 4446)
dev-postcap:
	@echo "Starting quarto preview for postcapitalism_after_ai at http://localhost:4446"
	cd research/postcapitalism_after_ai && uv run quarto preview

## dev: Alias for dev-calc (default course)
dev: dev-calc

## dev-notes: Live-reload Quartz notes site
dev-notes: sync-quartz-static
	@echo "Starting Quartz notes site with live reload ..."
	@echo "Open http://localhost:8080"
	cd quartz && npx quartz build --serve --port 8080

## sync-quartz-static: Overlay quartz/static/ (user assets) onto quartz/quartz/static/ (where Plugin.Static reads from)
# Quartz's Plugin.Static emitter reads from <quartz_install>/quartz/static/, NOT
# the top-level quartz/static/ that survives setup.sh. We keep our authoritative
# assets at the top level (so re-running setup.sh doesn't clobber them) and
# overlay them into the framework dir before each build.
sync-quartz-static:
	@cp -R quartz/static/. quartz/quartz/static/ 2>/dev/null || true

## build: Build all courses, research projects, and notes, stitch into _site/
build: build-books build-notes stitch

## preview: Build everything and serve _site/ at http://localhost:$(PORT)
preview: build
	@echo ""
	@echo "Serving $(SITE)/ at http://localhost:$(PORT)"
	@echo "Press Ctrl-C to stop."
	python3 -m http.server $(PORT) --directory $(SITE)

## build-books: Render all course and research books (uses freeze cache — only re-executes changed cells)
build-books:
	@for path in $(ALL_BOOKS); do \
		echo "==> Building $$path ..."; \
		(cd $$path && uv run quarto render --to html) || exit 1; \
	done

## build-calc: Build only the Calculation Course
build-calc:
	cd courses/the_calculation_course && uv run quarto render --to html

## build-notes: Build the Quartz notes site into quartz/public/
build-notes: sync-quartz-static
	@echo "==> Building Quartz notes site ..."
	cd quartz && npx quartz build

## stitch: Assemble _site/ from all build outputs
stitch:
	@echo "==> Stitching outputs into $(SITE)/ ..."
	rm -rf $(SITE)
	mkdir -p $(SITE)
	# Landing page at root
	cp site-root/index.html $(SITE)/index.html
	cp site-root/favicon.svg $(SITE)/favicon.svg
	# Each book at /<path>/ — path is courses/<name>/ or research/<name>/
	@for path in $(ALL_BOOKS); do \
		if [ -d "$$path/_book" ]; then \
			mkdir -p "$(SITE)/$$path"; \
			cp -r "$$path/_book/." "$(SITE)/$$path/"; \
			echo "  stitched: $$path"; \
		else \
			echo "  skipped (no _book/): $$path"; \
		fi; \
	done
	# Notes site at /notes/
	mkdir -p $(SITE)/notes
	cp -r quartz/public/. $(SITE)/notes/
	echo "  stitched: notes/"
	@echo ""
	@echo "$(SITE)/ is ready. Run 'make preview' to serve it."

## clean: Remove _site/ and all _book/ directories
clean:
	rm -rf $(SITE)
	@for path in $(ALL_BOOKS); do \
		rm -rf "$$path/_book"; \
		echo "  cleaned: $$path/_book"; \
	done
	rm -rf quartz/public
	@echo "Clean done."

## help: Show this help
help:
	@grep -E '^## ' Makefile | sed 's/^## //'
