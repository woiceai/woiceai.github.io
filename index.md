---
layout: default
title: WoiceAI platform
---

<div class="platform-intro">
  <p class="eyebrow">WoiceAI 2.0</p>
  <h1>Build assistants with your own knowledge</h1>
  <p>Turn documents, websites, audio and video into searchable knowledge. Build assistants that answer with sources, then connect them to visual workflows.</p>
  <p>Deploy the full project from <a href="https://github.com/asdkazmi/woiceai/tree/main">WoiceAI on main</a>.</p>
  {% assign start = site.pages | where: 'path', 'docs/getting-started/README.md' | first %}
  <a class="button" href="{{ start.url | relative_url }}">Get started <span aria-hidden="true">→</span></a>
</div>

<section aria-labelledby="platform-features">
  <h2 id="platform-features">Explore the platform</h2>
  <p class="section-description">See what each part of WoiceAI does and find its guide.</p>
  <div class="feature-grid">
    {% for feature in site.data.features %}
    {% assign guide = site.pages | where: 'path', feature.guide | first %}
    <article class="feature-card{% if feature.layout == 'portrait' %} feature-card--portrait{% endif %}">
      <div class="feature-image">
        <img src="{{ '/screenshorts/' | append: feature.image | relative_url }}" alt="{{ feature.alt | escape }}"{% unless forloop.first %} loading="lazy"{% endunless %}>
      </div>
      <div class="feature-copy">
        <h3>{{ feature.title | escape }}</h3>
        <p>{{ feature.overview | escape }}</p>
        <a href="{{ guide.url | relative_url }}{% if feature.anchor %}#{{ feature.anchor }}{% endif %}">Read the guide <span aria-hidden="true">→</span><span class="sr-only"> to {{ feature.title | escape }}</span></a>
      </div>
    </article>
    {% endfor %}
  </div>
</section>
