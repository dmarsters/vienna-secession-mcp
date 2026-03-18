# Vienna Secession Aesthetic MCP Server

Five-dimensional coordinate space for the Vienna Secession movement (1897–c.1910), covering painting, graphic design, architecture, and applied arts across the full range from Klimt's golden phase to Hoffmann's proto-modern geometry.

## Coordinate Space

| Axis | Description | Low (0.0) | High (1.0) |
|------|-------------|-----------|------------|
| `geometric_rigidity` | Organic fluidity ↔ rectilinear structure | Sinuous Art Nouveau curves, tendril forms | Pure grid, checkerboard, cubic volumes |
| `ornamental_density` | Surface saturation — negative space ↔ horror vacui | Austere white fields, single focal element | Every surface carries pattern, mosaic, metallic treatment |
| `material_preciousness` | Matte craft ↔ metallic opulence | Ink on paper, unfinished wood, plaster | Gold leaf, mosaic tesserae, jewel encrustation |
| `symbolic_charge` | Pure decoration ↔ dense iconographic program | Checkerboard patterns, geometric wallpaper | Multi-layered mythological narrative, esoteric symbols |
| `temporal_register` | Archaic/ancient ↔ proto-modern | Byzantine, Egyptian, Mycenaean references | Anticipating Bauhaus, functionalism, De Stijl |

## Architecture

Three-layer cost-optimization:

- **Layer 1 (0 tokens):** Pure taxonomy lookup — canonical states, traditions, visual vocabulary, optical properties
- **Layer 2 (0 tokens):** Deterministic computation — distance metrics, trajectory interpolation, keyword decomposition, vocabulary extraction from coordinates
- **Layer 3 (~100-200 tokens):** Structured data assembly for Claude synthesis via `enhance_secession_prompt`

## Tools (15)

### Layer 1 — Taxonomy Lookup

| Tool | Description |
|------|-------------|
| `get_server_info` | Server metadata, dimension list, taxonomy counts |
| `get_canonical_states` | All 10 reference states with 5D coordinates |
| `get_card` | Single state lookup with optional tradition bias |
| `get_traditions` | 5 tradition biases (Klimt, Hoffmann, Moser, Olbrich, Werkstätte) |
| `get_visual_types` | 16 visual types with keywords, centers, optical properties |
| `get_visual_vocabulary` | Complete vocabulary: compositions, surfaces, motifs, colors, figures |
| `get_optical_properties` | Light interaction and depth behavior by coordinate range |
| `get_cross_domain_trajectories` | Mappings to 6 adjacent movements |

### Layer 2 — Deterministic Computation

| Tool | Description |
|------|-------------|
| `compute_card_distance` | Euclidean distance between two states, per-axis breakdown |
| `compute_card_trajectory` | Interpolation path through 5D space with visual type at each step |
| `find_nearby_cards` | Nearest neighbor lookup in coordinate space |
| `decompose_secession_intent` | Natural language → 5D coordinates via keyword matching |
| `generate_attractor_prompt` | Vocabulary extraction from raw coordinates (composite/split_view/sequence modes) |
| `get_domain_registry_config` | Integration config for aesthetics-dynamics-core composition |

### Layer 3 — Synthesis Pipeline

| Tool | Description |
|------|-------------|
| `enhance_secession_prompt` | Full pipeline: intent + state + tradition → structured enhancement data |

## Traditions

Coordinate biases named for primary practitioners:

| Tradition | Character |
|-----------|-----------|
| `klimt_painterly` | Organic flow, maximum gold, symbolic density, archaic register |
| `hoffmann_geometric` | Pure grid, minimal ornament, proto-modern, decorative not symbolic |
| `moser_graphic` | Balanced geometry, surface richness, flat materials, contemporary |
| `olbrich_architectural` | Structural geometry, concentrated ornament zones, symbolic focal points |
| `werkstatte_applied` | Grid-dominant, high craft materials, selective decoration |

## Canonical States

| State | geo | orn | mat | sym | tmp | Character |
|-------|-----|-----|-----|-----|-----|-----------|
| `golden_klimt` | 0.35 | 0.95 | 0.95 | 0.70 | 0.15 | Maximum gold, saturated ornament, archaic |
| `quadratl_hoffmann` | 0.95 | 0.25 | 0.50 | 0.10 | 0.85 | Pure grid, minimal, proto-modern |
| `ver_sacrum_print` | 0.55 | 0.45 | 0.15 | 0.40 | 0.70 | Graphic poster/magazine, ink on paper |
| `stoclet_frieze` | 0.60 | 0.85 | 0.90 | 0.75 | 0.20 | Monumental mosaic, tree of life |
| `werkstatte_silver` | 0.80 | 0.35 | 0.65 | 0.15 | 0.60 | Geometric metalwork, hammered craft |
| `beethoven_narrative` | 0.30 | 0.70 | 0.60 | 0.95 | 0.25 | Maximum symbolic program, mythological |
| `secession_dome` | 0.65 | 0.50 | 0.70 | 0.55 | 0.40 | Austere volume, concentrated gold crown |
| `japonisme_graphic` | 0.40 | 0.30 | 0.20 | 0.30 | 0.75 | Asymmetric, muted, reduced means |
| `mosaic_polychrome` | 0.55 | 0.90 | 0.80 | 0.45 | 0.30 | Full-spectrum tessellated surface |
| `late_geometric` | 0.90 | 0.50 | 0.55 | 0.20 | 0.90 | Approaching modernism, ornament as structure |

## Visual Vocabulary

**16 visual types** spanning the movement's full aesthetic range — from `golden_iconic` to `proto_modern`, each with keyword sets, 5D coordinate centers, optical properties, and color associations.

**10 compositional structures** with explicit geometric specifications: `frieze_band` (height:width ≥ 1:3), `central_icon` (bilateral symmetry on vertical axis), `grid_tessellation` (≥ 60% surface coverage), `frame_within_frame` (minimum 2 nested), `golden_field` (≥ 40% metallic ground), `vertical_panel` (height:width ≥ 2:1), `mosaic_dissolution`, `asymmetric_japonisme`, `concentrated_ornament_zone`, `bilateral_relief`.

**10 surface treatments:** gold_leaf_flat, gold_leaf_tooled, mosaic_tesserae, enamel_flat, hammered_metal, woodcut_grain, stained_glass_lead, lacquer_depth, patina_verdigris, ivory_inlay.

**13 ornamental motifs:** spiral_volute, laurel_wreath, checkerboard, tree_of_life, eye_motif, triangle_cluster, lotus_palmette, meander_greek_key, organic_tendril, gorgon_head, circle_in_square, fish_scale, stylized_rose.

**8 color registers:** byzantine_gold, ver_sacrum_graphic, klimt_flesh, werkstatte_white, mosaic_polychrome, copper_patina, stained_glass_jewel, japonisme_muted.

**7 figure treatments:** iconic_frontal, pattern_dissolution, naturalistic_face_abstract_body, silhouette_graphic, caryatid_column, embrace_merge, floating_ungrounded.

## Cross-Domain Trajectories

Interpolation paths to adjacent movements, each with coordinate shift description and interpolation character:

| Target | Key Shift |
|--------|-----------|
| Art Nouveau / Jugendstil | Decrease geometric_rigidity, increase organic motifs |
| Bauhaus | Rigidity → 1.0, ornament → 0.0, preciousness → 0.2 |
| Byzantine | Temporal register → 0.0, preciousness and symbolic charge → max |
| Japonisme | Increase temporal register, decrease density, asymmetric composition |
| Arts & Crafts | Decrease preciousness, maintain density, medieval register |
| Art Deco | Increase rigidity, maintain preciousness, contemporary register |

## Deployment

**FastMCP Cloud entrypoint:** `vienna_secession_mcp.py:mcp`

**Local execution:**
```bash
python __main__.py
```

**Dependencies:** None beyond FastMCP. All taxonomy data and computation is self-contained.

## Integration

`get_domain_registry_config` returns the domain signature for registration with the aesthetics-dynamics-core compositional system, including all canonical state coordinates and visual type centers for cross-domain trajectory computation.
