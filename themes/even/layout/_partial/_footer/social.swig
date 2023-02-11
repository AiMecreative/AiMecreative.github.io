{%- if theme.social -%}
  <div class="social-links">
    {%- for name, path in theme.social -%}
      {%- if path -%}
        {%- if name == 'email' -%}
          <a href="mailto:{{ path }}" class="iconfont icon-{{ name }}" title="{{ name }}"></a>
        {%- else -%}
          <a href="{{ url_for(path) }}" class="iconfont icon-{{ name }}" title="{{ name }}"></a>
        {%- endif -%}
      {%- endif -%}
    {%- endfor -%}
  </div>
{%- endif -%}
