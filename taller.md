---
layout: archive
title: "El Taller de Escritura"
permalink: /taller/
author_profile: true
---

Aquí es donde los datos descansan y la ficción toma el mando. Relatos cortos, ejercicios de estilo y avances de mi futura novela.

<div class="taller-container">
  {% for post in site.categories.escritura %}
    <a href="{{ post.url | relative_url }}" class="taller-card-link">
      <article class="taller-card">
        <div class="taller-card-content">
          <div class="taller-meta">
            <span class="taller-category">{{ post.categories | first | uppercase }}</span>
            <span class="taller-date">{{ post.date | date: "%d %b, %Y" }}</span>
          </div>
          
          <h2 class="taller-title">{{ post.title }}</h2>
          
          <p class="taller-excerpt">
            {{ post.content | strip_html | truncatewords: 30 }}
          </p>
          
          <div class="taller-footer">
            <span class="taller-author">Por: {{ post.author | default: site.author.name }}</span>
            <span class="taller-read-more">Seguir leyendo →</span>
          </div>
        </div>
      </article>
    </a>
  {% endfor %}
</div>
