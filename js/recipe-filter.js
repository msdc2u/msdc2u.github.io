// Recipe Filter Script - Dynamic count version
function filterRecipes() {
    const search = document.getElementById('searchInput').value.toLowerCase();
    const cards = document.querySelectorAll('.recipe-card');
    let visible = 0;

    cards.forEach(card => {
        const title = card.querySelector('h3').textContent.toLowerCase();
        const cat = card.dataset.cat || '';
        const costMatch = activeFilter === 'cost-low' ? card.querySelector('.cost-low') : true;
        const catMatch = !activeFilter || activeFilter === 'cost-low' || cat === activeFilter;
        const searchMatch = !search || title.includes(search);

        if (catMatch && searchMatch && costMatch) {
            card.classList.remove('hidden');
            visible++;
        } else {
            card.classList.add('hidden');
        }
    });

    const totalRecipes = document.querySelectorAll('.recipe-card').length;
    const resultsEl = document.getElementById('resultsCount');

    if (visible === totalRecipes) {
        resultsEl.textContent = `Showing all ${totalRecipes} recipes`;
    } else {
        resultsEl.textContent = `Showing ${visible} recipe${visible === 1 ? '' : 's'}`;
    }
}

// Keep the setFilter function as it was
function setFilter(cat) {
    activeFilter = activeFilter === cat ? '' : cat;
    document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
    if (activeFilter) {
        document.querySelectorAll('.chip').forEach(c => {
            if (c.textContent.trim() === activeFilter || c.getAttribute('onclick') === `setFilter('${activeFilter}')`) {
                c.classList.add('active');
            }
        });
    }
    filterRecipes();
}