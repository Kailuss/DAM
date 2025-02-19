module.exports = async (tp) => {
	// Obtiene la vista activa
	const view = app.workspace.activeLeaf?.view;
	if (!view || !view.file) return;

	// Obtiene los metadatos de la nota
	const metadata = app.metadataCache.getFileCache(view.file)?.frontmatter;

	// Si el metadato 'cssclass' es 'modo-lectura', cambia a modo lectura
	if (metadata && metadata.cssclass === "modo-lectura") {
		await view.setViewState({ state: { mode: "preview" } });
	}
};