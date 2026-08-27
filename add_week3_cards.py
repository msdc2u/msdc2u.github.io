file_path = r"C:\Users\testi\whatsfortea website files\all-recipes.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_cards = """        <a href="recipes/sticky-sausage-pepper-kebabs-homemade-chips.html" class="recipe-card" data-cat="Fakeaways">
          <div class="card-image"><img src="images/recipes/sticky-sausage-pepper-kebabs-homemade-chips.jpg" alt="" loading="lazy"></div>
          <div class="card-body">
            <span class="cat-tag">Fakeaways</span>
            <h3>Sticky Sausage &amp; Pepper Kebabs with Homemade Chips</h3>
            <div class="card-meta">
              <span class="cost-badge cost-low"><span class="cost-dot"></span>Low</span>
              <span class="serves">Serves 4</span>
            </div>
          </div>
        </a>
        <a href="recipes/chicken-thigh-bacon-tray-bake.html" class="recipe-card" data-cat="Traybakes">
          <div class="card-image"><img src="images/recipes/chicken-thigh-bacon-tray-bake.jpg" alt="" loading="lazy"></div>
          <div class="card-body">
            <span class="cat-tag">Traybakes</span>
            <h3>Chicken Thigh &amp; Bacon Tray Bake</h3>
            <div class="card-meta">
              <span class="cost-badge cost-low"><span class="cost-dot"></span>Low</span>
              <span class="serves">Serves 4</span>
            </div>
          </div>
        </a>
        <a href="recipes/beef-mince-loaded-jackets-cheese.html" class="recipe-card" data-cat="Comfort Food">
          <div class="card-image"><img src="images/recipes/beef-mince-loaded-jackets-cheese.jpg" alt="" loading="lazy"></div>
          <div class="card-body">
            <span class="cat-tag">Comfort Food</span>
            <h3>Beef Mince Loaded Jackets with Cheese</h3>
            <div class="card-meta">
              <span class="cost-badge cost-low"><span class="cost-dot"></span>Low</span>
              <span class="serves">Serves 4</span>
            </div>
          </div>
        </a>
        <a href="recipes/pork-mince-meatball-mozzarella-pasta-bake.html" class="recipe-card" data-cat="Pasta">
          <div class="card-image"><img src="images/recipes/pork-mince-meatball-mozzarella-pasta-bake.jpg" alt="" loading="lazy"></div>
          <div class="card-body">
            <span class="cat-tag">Pasta</span>
            <h3>Pork Mince Meatball and Mozzarella Pasta Bake</h3>
            <div class="card-meta">
              <span class="cost-badge cost-low"><span class="cost-dot"></span>Low</span>
              <span class="serves">Serves 4</span>
            </div>
          </div>
        </a>
        <a href="recipes/sweet-chilli-chicken-thigh-rice-bowl.html" class="recipe-card" data-cat="Rice Dishes">
          <div class="card-image"><img src="images/recipes/sweet-chilli-chicken-thigh-rice-bowl.jpg" alt="" loading="lazy"></div>
          <div class="card-body">
            <span class="cat-tag">Rice Dishes</span>
            <h3>Sweet Chilli Chicken Thigh Rice Bowl</h3>
            <div class="card-meta">
              <span class="cost-badge cost-low"><span class="cost-dot"></span>Low</span>
              <span class="serves">Serves 4</span>
            </div>
          </div>
        </a>
        <a href="recipes/fish-cakes-oven-saute-potatoes-broccoli.html" class="recipe-card" data-cat="Fish">
          <div class="card-image"><img src="images/recipes/fish-cakes-oven-saute-potatoes-broccoli.jpg" alt="" loading="lazy"></div>
          <div class="card-body">
            <span class="cat-tag">Fish</span>
            <h3>Fish Cakes with Oven Sauté Potatoes and Broccoli</h3>
            <div class="card-meta">
              <span class="cost-badge cost-low"><span class="cost-dot"></span>Low</span>
              <span class="serves">Serves 4</span>
            </div>
          </div>
        </a>
        <a href="recipes/creamy-bacon-tomato-pasta.html" class="recipe-card" data-cat="Pasta">
          <div class="card-image"><img src="images/recipes/creamy-bacon-tomato-pasta.jpg" alt="" loading="lazy"></div>
          <div class="card-body">
            <span class="cat-tag">Pasta</span>
            <h3>Creamy Bacon &amp; Tomato Pasta</h3>
            <div class="card-meta">
              <span class="cost-badge cost-low"><span class="cost-dot"></span>Low</span>
              <span class="serves">Serves 4</span>
            </div>
          </div>
        </a>
"""

anchor = '<div class="recipe-grid">'
if anchor in content:
    content = content.replace(anchor, anchor + "\n" + new_cards)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: 7 new cards added to the TOP of the grid")
else:
    print("ERROR: Could not find the recipe grid")
