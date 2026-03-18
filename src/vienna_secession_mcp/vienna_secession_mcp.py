"""
Vienna Secession Aesthetic MCP Server

Five-dimensional coordinate space for the Vienna Secession movement (1897–c.1910),
covering painting, graphic design, architecture, and applied arts.

Three-layer cost-optimization architecture:
  Layer 1 (0 tokens): Pure taxonomy lookup — cards, states, traditions, vocabulary
  Layer 2 (0 tokens): Deterministic computation — distance, trajectory, vocabulary extraction
  Layer 3 (~100-200 tokens): Structured data assembly for Claude synthesis
"""

from fastmcp import FastMCP
import json
import math
from typing import Optional

mcp = FastMCP("vienna_secession_mcp")

# =============================================================================
# TAXONOMY DATA
# =============================================================================

PARAMETER_NAMES = [
    "geometric_rigidity",
    "ornamental_density",
    "material_preciousness",
    "symbolic_charge",
    "temporal_register",
]

# --- Traditions (coordinate biases) ---

TRADITIONS = {
    "klimt_painterly": {
        "description": "Gustav Klimt's painterly aesthetic. Bias toward organic flow, maximum surface saturation, gold/precious materials, symbolic density, archaic temporal references.",
        "biases": {
            "geometric_rigidity": -0.15,
            "ornamental_density": +0.20,
            "material_preciousness": +0.25,
            "symbolic_charge": +0.15,
            "temporal_register": -0.10,
        },
    },
    "hoffmann_geometric": {
        "description": "Josef Hoffmann's geometric rationalism. Pure geometry, restrained ornament, craft-quality materials, minimal symbolism, proto-modern register.",
        "biases": {
            "geometric_rigidity": +0.25,
            "ornamental_density": -0.15,
            "material_preciousness": +0.05,
            "symbolic_charge": -0.20,
            "temporal_register": +0.15,
        },
    },
    "moser_graphic": {
        "description": "Koloman Moser's graphic design aesthetic. Balanced geometric control with surface richness, graphic/flat materials, moderate symbolism, contemporary register.",
        "biases": {
            "geometric_rigidity": +0.10,
            "ornamental_density": +0.10,
            "material_preciousness": -0.10,
            "symbolic_charge": +0.05,
            "temporal_register": +0.10,
        },
    },
    "olbrich_architectural": {
        "description": "Joseph Maria Olbrich's architectural vocabulary. Structural geometry with concentrated ornamental zones, material quality in service of architecture, symbolic program at key focal points.",
        "biases": {
            "geometric_rigidity": +0.15,
            "ornamental_density": 0.00,
            "material_preciousness": +0.10,
            "symbolic_charge": +0.10,
            "temporal_register": -0.05,
        },
    },
    "werkstatte_applied": {
        "description": "Wiener Werkstätte applied arts. Grid-dominant, selective decoration, high craft/material quality, decorative rather than symbolic, craft-revival orientation.",
        "biases": {
            "geometric_rigidity": +0.20,
            "ornamental_density": +0.05,
            "material_preciousness": +0.15,
            "symbolic_charge": -0.15,
            "temporal_register": +0.05,
        },
    },
}

# --- 10 Canonical States ---

CANONICAL_STATES = {
    "golden_klimt": {
        "coordinates": {
            "geometric_rigidity": 0.35,
            "ornamental_density": 0.95,
            "material_preciousness": 0.95,
            "symbolic_charge": 0.70,
            "temporal_register": 0.15,
        },
        "description": "Maximum gold, saturated ornament, archaic symbolic. Klimt's golden phase — The Kiss, Portrait of Adele Bloch-Bauer I.",
        "primary_visual_type": "golden_iconic",
    },
    "quadratl_hoffmann": {
        "coordinates": {
            "geometric_rigidity": 0.95,
            "ornamental_density": 0.25,
            "material_preciousness": 0.50,
            "symbolic_charge": 0.10,
            "temporal_register": 0.85,
        },
        "description": "Pure grid geometry, minimal ornament, proto-modern. Hoffmann's 'Quadratl' — checkerboard patterns, cubic furniture, rationalist architecture.",
        "primary_visual_type": "geometric_grid",
    },
    "ver_sacrum_print": {
        "coordinates": {
            "geometric_rigidity": 0.55,
            "ornamental_density": 0.45,
            "material_preciousness": 0.15,
            "symbolic_charge": 0.40,
            "temporal_register": 0.70,
        },
        "description": "Graphic poster/magazine aesthetic, ink on paper. Ver Sacrum publication design, woodcuts, lithographic prints.",
        "primary_visual_type": "graphic_print",
    },
    "stoclet_frieze": {
        "coordinates": {
            "geometric_rigidity": 0.60,
            "ornamental_density": 0.85,
            "material_preciousness": 0.90,
            "symbolic_charge": 0.75,
            "temporal_register": 0.20,
        },
        "description": "Monumental mosaic, tree of life, architectural integration. Klimt's Stoclet Palace frieze — marble, gold, semi-precious stone inlay.",
        "primary_visual_type": "monumental_mosaic",
    },
    "werkstatte_silver": {
        "coordinates": {
            "geometric_rigidity": 0.80,
            "ornamental_density": 0.35,
            "material_preciousness": 0.65,
            "symbolic_charge": 0.15,
            "temporal_register": 0.60,
        },
        "description": "Geometric metalwork, hammered craft, selective ornament. Wiener Werkstätte silver services, cutlery, decorative objects.",
        "primary_visual_type": "craft_metalwork",
    },
    "beethoven_narrative": {
        "coordinates": {
            "geometric_rigidity": 0.30,
            "ornamental_density": 0.70,
            "material_preciousness": 0.60,
            "symbolic_charge": 0.95,
            "temporal_register": 0.25,
        },
        "description": "Maximum symbolic program, frieze narrative, mythological. Klimt's Beethoven Frieze — hostile forces, knight, redemption, embrace.",
        "primary_visual_type": "narrative_frieze",
    },
    "secession_dome": {
        "coordinates": {
            "geometric_rigidity": 0.65,
            "ornamental_density": 0.50,
            "material_preciousness": 0.70,
            "symbolic_charge": 0.55,
            "temporal_register": 0.40,
        },
        "description": "Architectural landmark — austere volume, concentrated gold crown. Olbrich's Secession Building with laurel-leaf dome.",
        "primary_visual_type": "architectural_monument",
    },
    "japonisme_graphic": {
        "coordinates": {
            "geometric_rigidity": 0.40,
            "ornamental_density": 0.30,
            "material_preciousness": 0.20,
            "symbolic_charge": 0.30,
            "temporal_register": 0.75,
        },
        "description": "Asymmetric, muted, contemporary-register, reduced means. Japanese woodblock influence on Secession graphic design.",
        "primary_visual_type": "japonisme_flat",
    },
    "mosaic_polychrome": {
        "coordinates": {
            "geometric_rigidity": 0.55,
            "ornamental_density": 0.90,
            "material_preciousness": 0.80,
            "symbolic_charge": 0.45,
            "temporal_register": 0.30,
        },
        "description": "Full-spectrum tessellated surface, decorative over symbolic. Mosaic work — turquoise, coral, amber, violet, jade in small units.",
        "primary_visual_type": "tessellated_surface",
    },
    "late_geometric": {
        "coordinates": {
            "geometric_rigidity": 0.90,
            "ornamental_density": 0.50,
            "material_preciousness": 0.55,
            "symbolic_charge": 0.20,
            "temporal_register": 0.90,
        },
        "description": "Approaching modernism — geometry dominant, ornament as structure. Late Hoffmann, proto-Bauhaus reduction.",
        "primary_visual_type": "proto_modern",
    },
    "organic_nouveau": {
        "coordinates": {
            "geometric_rigidity": 0.15,
            "ornamental_density": 0.65,
            "material_preciousness": 0.50,
            "symbolic_charge": 0.45,
            "temporal_register": 0.50,
        },
        "description": "Maximum organic flow — whiplash curves, vine tendrils, botanical sinuosity. The Secession's Art Nouveau inheritance before geometric rationalism prevailed.",
        "primary_visual_type": "organic_nouveau",
    },
}

# --- Visual Types with Keywords and 5D Centers ---

VISUAL_TYPES = {
    # --- High ornament, high preciousness ---
    "golden_iconic": {
        "keywords": ["gold", "golden", "leaf", "byzantine", "opulent", "radiant", "precious", "metallic", "sacred", "hieratic"],
        "center": {"geometric_rigidity": 0.35, "ornamental_density": 0.95, "material_preciousness": 0.95, "symbolic_charge": 0.70, "temporal_register": 0.15},
        "optical": {"reflectance": "full_metallic", "depth": "total_flatness", "light": "gold_leaf_mirror_plane"},
        "color_associations": ["gold", "deep_blue_lapis", "crimson", "emerald"],
    },
    "monumental_mosaic": {
        "keywords": ["mosaic", "tesserae", "monumental", "inlay", "stone", "marble", "frieze", "mural", "wall"],
        "center": {"geometric_rigidity": 0.60, "ornamental_density": 0.85, "material_preciousness": 0.90, "symbolic_charge": 0.75, "temporal_register": 0.20},
        "optical": {"reflectance": "multi_angle_scatter", "depth": "shallow_relief", "light": "tesserae_sparkle"},
        "color_associations": ["gold", "turquoise", "coral", "deep_brown", "cream"],
    },
    "tessellated_surface": {
        "keywords": ["tessellated", "polychrome", "colorful", "pattern", "tiled", "allover", "decorative", "mosaic_field"],
        "center": {"geometric_rigidity": 0.55, "ornamental_density": 0.90, "material_preciousness": 0.80, "symbolic_charge": 0.45, "temporal_register": 0.30},
        "optical": {"reflectance": "specular_translucent", "depth": "compressed_flatness", "light": "polychrome_scatter"},
        "color_associations": ["turquoise", "coral", "amber", "violet", "jade"],
    },
    # --- Geometric dominant ---
    "geometric_grid": {
        "keywords": ["grid", "checkerboard", "square", "cubic", "rational", "minimal", "pure", "quadratl", "rectilinear"],
        "center": {"geometric_rigidity": 0.95, "ornamental_density": 0.25, "material_preciousness": 0.50, "symbolic_charge": 0.10, "temporal_register": 0.85},
        "optical": {"reflectance": "satin", "depth": "deep_spatial", "light": "even_diffuse"},
        "color_associations": ["white", "black", "silver", "single_accent"],
    },
    "proto_modern": {
        "keywords": ["modern", "functionalist", "reduced", "bauhaus", "abstract", "stripped", "austere", "structural"],
        "center": {"geometric_rigidity": 0.90, "ornamental_density": 0.50, "material_preciousness": 0.55, "symbolic_charge": 0.20, "temporal_register": 0.90},
        "optical": {"reflectance": "satin", "depth": "deep_spatial", "light": "clean_directional"},
        "color_associations": ["white", "grey", "black", "teal_accent"],
    },
    "craft_metalwork": {
        "keywords": ["silver", "hammered", "metal", "craft", "cutlery", "werkstatte", "forged", "smithed", "service"],
        "center": {"geometric_rigidity": 0.80, "ornamental_density": 0.35, "material_preciousness": 0.65, "symbolic_charge": 0.15, "temporal_register": 0.60},
        "optical": {"reflectance": "directional_sheen", "depth": "shallow_relief", "light": "hammered_catch_light"},
        "color_associations": ["silver", "warm_grey", "polished_steel", "ebony"],
    },
    # --- Graphic / print ---
    "graphic_print": {
        "keywords": ["print", "woodcut", "lithograph", "poster", "magazine", "ink", "graphic", "publication", "editorial"],
        "center": {"geometric_rigidity": 0.55, "ornamental_density": 0.45, "material_preciousness": 0.15, "symbolic_charge": 0.40, "temporal_register": 0.70},
        "optical": {"reflectance": "matte_absorption", "depth": "total_flatness", "light": "high_contrast_ink"},
        "color_associations": ["black", "white", "red_accent", "cream"],
    },
    "japonisme_flat": {
        "keywords": ["japanese", "asymmetric", "ukiyo", "floating", "muted", "woodblock", "cropped", "negative_space", "zen"],
        "center": {"geometric_rigidity": 0.40, "ornamental_density": 0.30, "material_preciousness": 0.20, "symbolic_charge": 0.30, "temporal_register": 0.75},
        "optical": {"reflectance": "matte_absorption", "depth": "compressed_flatness", "light": "soft_ambient"},
        "color_associations": ["soft_grey", "sage", "dusty_rose", "ink_black", "cream"],
    },
    # --- Narrative / symbolic ---
    "narrative_frieze": {
        "keywords": ["narrative", "story", "mythological", "allegory", "processional", "epic", "heroic", "symbolic_program"],
        "center": {"geometric_rigidity": 0.30, "ornamental_density": 0.70, "material_preciousness": 0.60, "symbolic_charge": 0.95, "temporal_register": 0.25},
        "optical": {"reflectance": "mixed_satin_metallic", "depth": "shallow_relief", "light": "dramatic_directional"},
        "color_associations": ["gold", "warm_ochre", "dark_brown", "pale_flesh", "crimson"],
    },
    # --- Architectural ---
    "architectural_monument": {
        "keywords": ["building", "architecture", "dome", "facade", "portal", "monument", "edifice", "temple", "pavilion"],
        "center": {"geometric_rigidity": 0.65, "ornamental_density": 0.50, "material_preciousness": 0.70, "symbolic_charge": 0.55, "temporal_register": 0.40},
        "optical": {"reflectance": "specular_translucent", "depth": "deep_spatial", "light": "natural_daylight"},
        "color_associations": ["white_plaster", "gold_dome", "verdigris", "warm_stone"],
    },
    "concentrated_portal": {
        "keywords": ["doorway", "entrance", "portal", "threshold", "gateway", "inscription", "concentrated", "focal"],
        "center": {"geometric_rigidity": 0.70, "ornamental_density": 0.45, "material_preciousness": 0.60, "symbolic_charge": 0.60, "temporal_register": 0.45},
        "optical": {"reflectance": "mixed_satin_metallic", "depth": "deep_spatial", "light": "shadow_contrast"},
        "color_associations": ["warm_stone", "gold_inscription", "deep_shadow", "white"],
    },
    # --- Organic / flowing ---
    "organic_nouveau": {
        "keywords": ["organic", "flowing", "vine", "tendril", "sinuous", "whiplash", "botanical", "floral", "natural", "curving"],
        "center": {"geometric_rigidity": 0.15, "ornamental_density": 0.65, "material_preciousness": 0.50, "symbolic_charge": 0.45, "temporal_register": 0.50},
        "optical": {"reflectance": "satin", "depth": "shallow_relief", "light": "soft_ambient"},
        "color_associations": ["sage_green", "warm_gold", "ivory", "deep_brown"],
    },
    # --- Glass / translucent ---
    "stained_glass_jewel": {
        "keywords": ["glass", "stained", "translucent", "jewel", "window", "lead", "came", "luminous", "cathedral"],
        "center": {"geometric_rigidity": 0.55, "ornamental_density": 0.70, "material_preciousness": 0.70, "symbolic_charge": 0.50, "temporal_register": 0.35},
        "optical": {"reflectance": "transmitted_glow", "depth": "compressed_flatness", "light": "backlit_color"},
        "color_associations": ["cobalt", "ruby", "emerald", "amber", "black_leading"],
    },
    # --- Textile / surface pattern ---
    "textile_pattern": {
        "keywords": ["textile", "fabric", "weave", "pattern", "repeat", "wallpaper", "carpet", "tapestry", "cloth"],
        "center": {"geometric_rigidity": 0.60, "ornamental_density": 0.75, "material_preciousness": 0.40, "symbolic_charge": 0.20, "temporal_register": 0.55},
        "optical": {"reflectance": "diffuse_absorption", "depth": "total_flatness", "light": "even_diffuse"},
        "color_associations": ["indigo", "cream", "gold_thread", "sage", "burgundy"],
    },
    # --- Enamel / lacquer ---
    "enamel_precious": {
        "keywords": ["enamel", "lacquer", "cloisonne", "glossy", "jewel_box", "precious_object", "miniature", "cabinet"],
        "center": {"geometric_rigidity": 0.65, "ornamental_density": 0.80, "material_preciousness": 0.85, "symbolic_charge": 0.35, "temporal_register": 0.30},
        "optical": {"reflectance": "specular_gloss", "depth": "lacquer_depth", "light": "enamel_sheen"},
        "color_associations": ["deep_blue", "emerald", "gold_wire", "black_lacquer", "coral"],
    },
    # --- Patina / aged ---
    "patina_aged": {
        "keywords": ["patina", "aged", "verdigris", "oxidized", "weathered", "copper", "bronze", "antique", "time"],
        "center": {"geometric_rigidity": 0.50, "ornamental_density": 0.40, "material_preciousness": 0.40, "symbolic_charge": 0.35, "temporal_register": 0.35},
        "optical": {"reflectance": "satin_matte", "depth": "shallow_relief", "light": "diffuse_warm"},
        "color_associations": ["verdigris_green", "warm_copper", "oxidized_brown", "aged_cream"],
    },
}

# --- Compositional Geometry ---

COMPOSITIONAL_STRUCTURES = {
    "frieze_band": {
        "specification": "Horizontal register division. Subject contained within parallel horizontal boundaries. Height:width ratio >= 1:3.",
        "affinity": {"geometric_rigidity": (0.4, 1.0)},
        "keywords": ["frieze", "band", "horizontal", "register", "processional"],
    },
    "central_icon": {
        "specification": "Single figure/motif centered on vertical axis, bilateral symmetry, flanked by decorative fields.",
        "affinity": {"symbolic_charge": (0.5, 1.0)},
        "keywords": ["central", "icon", "frontal", "symmetric", "hieratic"],
    },
    "grid_tessellation": {
        "specification": "Regular repeating unit cell. Square, hexagonal, or triangular tiling covering >= 60% of surface.",
        "affinity": {"geometric_rigidity": (0.7, 1.0), "ornamental_density": (0.6, 1.0)},
        "keywords": ["grid", "tessellation", "tiling", "repeat", "allover"],
    },
    "frame_within_frame": {
        "specification": "Rectilinear border containing secondary border containing subject. Minimum 2 nested frames.",
        "affinity": {"geometric_rigidity": (0.5, 1.0)},
        "keywords": ["frame", "nested", "border", "contained", "layered"],
    },
    "golden_field": {
        "specification": "Flat metallic ground plane occupying >= 40% of composition, figures emerging from/dissolving into it.",
        "affinity": {"material_preciousness": (0.7, 1.0)},
        "keywords": ["golden", "field", "ground", "metallic", "dissolving"],
    },
    "vertical_panel": {
        "specification": "Tall narrow format, height:width ratio >= 2:1. Stacked registers or single ascending figure.",
        "affinity": {"geometric_rigidity": (0.3, 1.0)},
        "keywords": ["vertical", "panel", "tall", "narrow", "ascending"],
    },
    "mosaic_dissolution": {
        "specification": "Figure/ground boundary dissolved into tessellated pattern. Subject merges with decorative field.",
        "affinity": {"ornamental_density": (0.7, 1.0), "geometric_rigidity": (0.4, 1.0)},
        "keywords": ["dissolution", "merge", "tessellated", "boundary", "figure_ground"],
    },
    "asymmetric_japonisme": {
        "specification": "Off-center composition, diagonal flow, cropped elements, empty space as active element.",
        "affinity": {"temporal_register": (0.6, 1.0), "geometric_rigidity": (0.0, 0.4)},
        "keywords": ["asymmetric", "off_center", "diagonal", "cropped", "negative_space"],
    },
    "concentrated_ornament_zone": {
        "specification": "Austere surfaces framing single zone of intense ornamental focus. Overall density low, local density maximum.",
        "affinity": {"ornamental_density": (0.3, 0.6)},
        "keywords": ["concentrated", "focal", "zone", "contrast", "portal"],
    },
    "bilateral_relief": {
        "specification": "Mirror-symmetric composition in shallow depth. Paired elements flanking central axis, bas-relief spatial logic.",
        "affinity": {"geometric_rigidity": (0.5, 0.8), "symbolic_charge": (0.4, 1.0)},
        "keywords": ["bilateral", "symmetric", "relief", "paired", "flanking"],
    },
}

# --- Surface Treatments ---

SURFACE_TREATMENTS = {
    "gold_leaf_flat": {
        "specification": "Uniform metallic gold surface, no modulation, reflective plane.",
        "affinity": {"material_preciousness": (0.8, 1.0)},
        "keywords": ["gold_leaf", "flat_gold", "uniform_metallic"],
    },
    "gold_leaf_tooled": {
        "specification": "Gold surface with incised/stamped geometric pattern — spirals, circles, rectangles.",
        "affinity": {"material_preciousness": (0.8, 1.0), "ornamental_density": (0.6, 1.0)},
        "keywords": ["tooled", "incised", "stamped", "patterned_gold"],
    },
    "mosaic_tesserae": {
        "specification": "Small discrete color units (square, triangular, irregular) composing larger image.",
        "affinity": {"material_preciousness": (0.6, 1.0), "ornamental_density": (0.7, 1.0)},
        "keywords": ["tesserae", "mosaic_units", "discrete_color"],
    },
    "enamel_flat": {
        "specification": "Smooth, glossy, saturated color fields with hard edges.",
        "affinity": {"material_preciousness": (0.5, 1.0), "geometric_rigidity": (0.5, 1.0)},
        "keywords": ["enamel", "glossy", "saturated_field", "hard_edge"],
    },
    "hammered_metal": {
        "specification": "Visible tool marks on metallic surface, matte-to-satin finish.",
        "affinity": {"material_preciousness": (0.3, 0.6)},
        "keywords": ["hammered", "tool_marks", "satin_metal"],
    },
    "woodcut_grain": {
        "specification": "Visible linear grain, high contrast, ink-on-paper flatness.",
        "affinity": {"material_preciousness": (0.0, 0.3)},
        "keywords": ["woodcut", "grain", "ink", "high_contrast", "paper"],
    },
    "stained_glass_lead": {
        "specification": "Color fields bounded by dark linear network (lead came), transmitted light effect.",
        "affinity": {"material_preciousness": (0.5, 0.8), "geometric_rigidity": (0.5, 1.0)},
        "keywords": ["stained_glass", "lead_came", "transmitted_light"],
    },
    "lacquer_depth": {
        "specification": "Deep, layered gloss surface suggesting depth beneath reflective plane.",
        "affinity": {"material_preciousness": (0.5, 0.7)},
        "keywords": ["lacquer", "deep_gloss", "layered_surface"],
    },
    "patina_verdigris": {
        "specification": "Aged copper-green oxidation, time-marked surface.",
        "affinity": {"material_preciousness": (0.3, 0.5), "temporal_register": (0.0, 0.4)},
        "keywords": ["patina", "verdigris", "oxidized", "aged"],
    },
    "ivory_inlay": {
        "specification": "Pale organic material set into darker ground, geometric or figural.",
        "affinity": {"material_preciousness": (0.7, 1.0), "geometric_rigidity": (0.5, 1.0)},
        "keywords": ["ivory", "inlay", "bone", "contrast_insert"],
    },
}

# --- Ornamental Motifs ---

ORNAMENTAL_MOTIFS = {
    "spiral_volute": {"keywords": ["spiral", "volute", "logarithmic", "scroll", "curl"], "affinity": {"geometric_rigidity": (0.3, 0.6)}},
    "laurel_wreath": {"keywords": ["laurel", "wreath", "crown", "victory", "leaf_ring"], "affinity": {"symbolic_charge": (0.4, 1.0), "temporal_register": (0.0, 0.5)}},
    "checkerboard": {"keywords": ["checkerboard", "check", "alternating", "squares"], "affinity": {"geometric_rigidity": (0.8, 1.0), "ornamental_density": (0.4, 1.0)}},
    "tree_of_life": {"keywords": ["tree", "life", "branches", "trunk", "stoclet"], "affinity": {"symbolic_charge": (0.6, 1.0), "geometric_rigidity": (0.4, 0.7)}},
    "eye_motif": {"keywords": ["eye", "gaze", "watching", "ocular", "all_seeing"], "affinity": {"symbolic_charge": (0.7, 1.0)}},
    "triangle_cluster": {"keywords": ["triangle", "equilateral", "pyramid", "angular"], "affinity": {"geometric_rigidity": (0.7, 1.0)}},
    "lotus_palmette": {"keywords": ["lotus", "palmette", "fan", "egyptian", "palm"], "affinity": {"temporal_register": (0.0, 0.3), "symbolic_charge": (0.3, 1.0)}},
    "meander_greek_key": {"keywords": ["meander", "greek_key", "fret", "labyrinth", "maze"], "affinity": {"geometric_rigidity": (0.7, 1.0), "temporal_register": (0.0, 0.3)}},
    "organic_tendril": {"keywords": ["tendril", "vine", "stem", "climbing", "whiplash"], "affinity": {"geometric_rigidity": (0.0, 0.3), "ornamental_density": (0.4, 1.0)}},
    "gorgon_head": {"keywords": ["gorgon", "medusa", "apotropaic", "mask", "frontal_face"], "affinity": {"symbolic_charge": (0.8, 1.0), "temporal_register": (0.0, 0.3)}},
    "circle_in_square": {"keywords": ["circle_square", "inscribed", "mandala", "contained_circle"], "affinity": {"geometric_rigidity": (0.6, 1.0)}},
    "fish_scale": {"keywords": ["fish_scale", "scallop", "imbricated", "overlapping_arc"], "affinity": {"ornamental_density": (0.5, 1.0), "geometric_rigidity": (0.4, 0.7)}},
    "stylized_rose": {"keywords": ["rose", "rosette", "concentric_petals", "geometric_flower"], "affinity": {"geometric_rigidity": (0.4, 0.7), "symbolic_charge": (0.3, 0.6)}},
}

# --- Color Registers ---

COLOR_REGISTERS = {
    "byzantine_gold": {
        "palette": ["gold", "deep_blue_lapis", "crimson", "emerald", "gold_ground"],
        "affinity": {"material_preciousness": (0.8, 1.0), "temporal_register": (0.0, 0.3)},
    },
    "ver_sacrum_graphic": {
        "palette": ["black", "white", "red_accent", "high_contrast", "ink_derived"],
        "affinity": {"material_preciousness": (0.0, 0.3), "temporal_register": (0.6, 1.0)},
    },
    "klimt_flesh": {
        "palette": ["gold", "warm_ochre", "rose_pink", "pale_green", "deep_brown"],
        "affinity": {"material_preciousness": (0.6, 1.0), "symbolic_charge": (0.5, 1.0)},
    },
    "werkstatte_white": {
        "palette": ["white", "black", "silver", "single_accent_violet_or_teal"],
        "affinity": {"geometric_rigidity": (0.7, 1.0), "ornamental_density": (0.0, 0.4)},
    },
    "mosaic_polychrome": {
        "palette": ["turquoise", "coral", "amber", "violet", "jade", "tessellated_units"],
        "affinity": {"ornamental_density": (0.7, 1.0), "material_preciousness": (0.6, 1.0)},
    },
    "copper_patina": {
        "palette": ["verdigris_green", "warm_copper", "oxidized_brown", "aged_cream"],
        "affinity": {"material_preciousness": (0.3, 0.6), "temporal_register": (0.3, 0.5)},
    },
    "stained_glass_jewel": {
        "palette": ["cobalt", "ruby", "emerald", "amber", "black_leading"],
        "affinity": {"material_preciousness": (0.5, 0.8), "geometric_rigidity": (0.5, 1.0)},
    },
    "japonisme_muted": {
        "palette": ["soft_grey", "sage", "dusty_rose", "ink_black", "cream"],
        "affinity": {"temporal_register": (0.6, 1.0), "ornamental_density": (0.0, 0.5)},
    },
}

# --- Figure Treatments ---

FIGURE_TREATMENTS = {
    "iconic_frontal": {
        "specification": "Figure facing viewer directly, symmetrical pose, hieratic.",
        "affinity": {"symbolic_charge": (0.6, 1.0), "temporal_register": (0.0, 0.4)},
        "keywords": ["frontal", "hieratic", "icon", "symmetrical_pose"],
    },
    "pattern_dissolution": {
        "specification": "Figure's clothing/body merges into surrounding decorative field — where does body end and ornament begin?",
        "affinity": {"ornamental_density": (0.7, 1.0)},
        "keywords": ["dissolution", "merge", "pattern_body", "figure_ground_ambiguity"],
    },
    "naturalistic_face_abstract_body": {
        "specification": "Realistic head/hands emerging from flat decorative body/garment. Klimt signature treatment.",
        "affinity": {"ornamental_density": (0.5, 1.0), "symbolic_charge": (0.4, 1.0)},
        "keywords": ["face_realistic", "body_abstract", "klimt_figure", "decorative_garment"],
    },
    "silhouette_graphic": {
        "specification": "Figure reduced to flat profile, no interior modeling.",
        "affinity": {"material_preciousness": (0.0, 0.3), "geometric_rigidity": (0.5, 1.0)},
        "keywords": ["silhouette", "profile", "flat", "graphic_figure"],
    },
    "caryatid_column": {
        "specification": "Figure functioning as architectural support, elongated, vertical.",
        "affinity": {"geometric_rigidity": (0.5, 1.0), "symbolic_charge": (0.5, 1.0)},
        "keywords": ["caryatid", "column_figure", "architectural_support", "elongated"],
    },
    "embrace_merge": {
        "specification": "Two figures interlocking, boundaries dissolving, shared ornamental field.",
        "affinity": {"symbolic_charge": (0.7, 1.0), "ornamental_density": (0.6, 1.0)},
        "keywords": ["embrace", "interlock", "merge", "couple", "kiss"],
    },
    "floating_ungrounded": {
        "specification": "Figure suspended without ground plane, surrounded by gold or pattern field.",
        "affinity": {"material_preciousness": (0.6, 1.0)},
        "keywords": ["floating", "suspended", "ungrounded", "hovering", "gold_field"],
    },
}

# --- Optical Properties ---

OPTICAL_PROPERTIES = {
    "reflectance_by_preciousness": [
        {"range": (0.0, 0.2), "behavior": "Diffuse absorption. Matte surfaces, ink-dark contrasts, paper-white reflectance."},
        {"range": (0.3, 0.5), "behavior": "Satin reflectance. Directional sheen on wood, hammered metal catch-light."},
        {"range": (0.6, 0.8), "behavior": "Specular + translucent. Enamel gloss, stained glass transmitted glow, polished metal reflection."},
        {"range": (0.9, 1.0), "behavior": "Full metallic reflectance. Gold leaf mirror-plane, mosaic tesserae multi-angle scatter, jewel refraction."},
    ],
    "depth_by_density": [
        {"range": (0.0, 0.3), "behavior": "Deep spatial recession. Architecture reads as volume in space."},
        {"range": (0.4, 0.6), "behavior": "Shallow relief. Layered planes at slight offsets, bas-relief depth."},
        {"range": (0.7, 0.8), "behavior": "Compressed flatness. Pattern fills push toward picture plane."},
        {"range": (0.9, 1.0), "behavior": "Total flatness. Pure surface — no spatial recession, all-over decorative field."},
    ],
}

# --- Cross-Domain Trajectory Mappings ---

CROSS_DOMAIN_TRAJECTORIES = {
    "to_art_nouveau": {
        "target_movement": "Art Nouveau / Jugendstil",
        "coordinate_shift": "Decrease geometric_rigidity, increase organic_tendril motifs, maintain ornamental_density.",
        "interpolation_character": "Rectilinear frames soften into whiplash curves. Grid structures dissolve into flowing organic networks.",
    },
    "to_bauhaus": {
        "target_movement": "Bauhaus",
        "coordinate_shift": "Increase geometric_rigidity to 1.0, decrease ornamental_density to 0.0, material_preciousness to 0.2.",
        "interpolation_character": "Ornament progressively stripped. Gold becomes white. Symbolic content evacuated. Pure function emerges.",
    },
    "to_byzantine": {
        "target_movement": "Byzantine",
        "coordinate_shift": "Decrease temporal_register to 0.0, increase material_preciousness and symbolic_charge to maximum.",
        "interpolation_character": "Contemporary elements recede. Gold ground intensifies. Figures become fully hieratic. Mosaic logic dominates.",
    },
    "to_japonisme": {
        "target_movement": "Japonisme / Ukiyo-e",
        "coordinate_shift": "Increase temporal_register, decrease ornamental_density, shift to asymmetric composition.",
        "interpolation_character": "Symmetry breaks. Density thins. Active negative space appears. Cropping introduces diagonal flow.",
    },
    "to_arts_and_crafts": {
        "target_movement": "Arts & Crafts Movement",
        "coordinate_shift": "Decrease material_preciousness, maintain ornamental_density, shift temporal_register toward medieval.",
        "interpolation_character": "Gold yields to wood and textile. Craft remains but preciousness diminishes. Gothic structural logic emerges.",
    },
    "to_art_deco": {
        "target_movement": "Art Deco",
        "coordinate_shift": "Increase geometric_rigidity, maintain material_preciousness, shift temporal_register toward contemporary.",
        "interpolation_character": "Organic curves sharpen into chevrons and zigzags. Gold persists but geometry hardens. Machine aesthetic enters.",
    },
}


# =============================================================================
# PHASE 2.6 — RHYTHMIC PRESETS
# =============================================================================
# Period strategy for cross-domain composition:
#   Period 14 → GAP-FILLER (fills 12–15 gap), novel LCM harmonics
#   Period 15 → synchronizes with nuclear, catastrophe, diatom
#   Period 18 → synchronizes with nuclear, catastrophe, diatom
#   Period 22 → synchronizes with catastrophe, heraldic
#   Period 24 → synchronizes with microscopy
#   Period 28 → reinforces discovered composite-beat attractor (60−2×16)
#   Period 30 → reinforces dominant Period 30 LCM hub

RHYTHMIC_PRESETS = {
    "secession_breathing": {
        "description": "Architectural monument dissolves into organic flow and reconstitutes. "
                       "Olbrich's rational dome breathes into Nouveau tendrils.",
        "state_a": "secession_dome",
        "state_b": "organic_nouveau",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 14,
        "period_rationale": "Gap-filler: fills empty 12–15 period gap. Creates novel LCM "
                            "harmonics with Period 12 (LCM=84) and Period 15 (LCM=210).",
    },
    "craft_cycle": {
        "description": "Wiener Werkstätte hammered silver oscillates with Ver Sacrum "
                       "graphic print. Precious material meets ink austerity.",
        "state_a": "werkstatte_silver",
        "state_b": "ver_sacrum_print",
        "pattern": "sinusoidal",
        "num_cycles": 4,
        "steps_per_cycle": 15,
        "period_rationale": "Synchronizes with nuclear (15), catastrophe (15), diatom (15). "
                            "3-domain lock at Period 15 for cross-domain resonance.",
    },
    "material_oscillation": {
        "description": "Japanese restraint meets Klimtian opulence. Muted ink-wash "
                       "austerity swells into full golden iconic splendor.",
        "state_a": "japonisme_graphic",
        "state_b": "golden_klimt",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 18,
        "period_rationale": "Synchronizes with nuclear (18), catastrophe (18), diatom (18). "
                            "Maximum material-axis sweep across full preciousness range.",
    },
    "symbolic_pulse": {
        "description": "Hoffmann's pure rationalism confronts Klimt's Beethoven Frieze "
                       "narrative program. Geometry yields to myth and returns.",
        "state_a": "quadratl_hoffmann",
        "state_b": "beethoven_narrative",
        "pattern": "triangular",
        "num_cycles": 3,
        "steps_per_cycle": 22,
        "period_rationale": "Synchronizes with catastrophe (22), heraldic (22). "
                            "Triangular pattern creates sharp symbolic–geometric transitions.",
    },
    "ornament_rhythm": {
        "description": "Full polychrome mosaic surface pulses against late geometric "
                       "reduction. Maximum ornamental density sweeps to proto-modern restraint.",
        "state_a": "mosaic_polychrome",
        "state_b": "late_geometric",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 24,
        "period_rationale": "Synchronizes with microscopy (24). Spans full ornamental-density "
                            "axis from 0.90 to 0.50.",
    },
    "epoch_sweep": {
        "description": "Stoclet Palace monumental mosaic evolves toward late geometric "
                       "modernism. Archaic preciousness yields to functionalist clarity.",
        "state_a": "stoclet_frieze",
        "state_b": "late_geometric",
        "pattern": "sinusoidal",
        "num_cycles": 2,
        "steps_per_cycle": 28,
        "period_rationale": "Reinforces Period 28 composite-beat attractor (60−2×16). "
                            "Long sweep covers full temporal-register axis.",
    },
    "golden_convergence": {
        "description": "Maximum aesthetic distance: Klimt golden icon oscillates with "
                       "Hoffmann grid rationalism. The central tension of the Secession.",
        "state_a": "golden_klimt",
        "state_b": "quadratl_hoffmann",
        "pattern": "sinusoidal",
        "num_cycles": 2,
        "steps_per_cycle": 30,
        "period_rationale": "Reinforces dominant Period 30 LCM hub (microscopy+diatom+heraldic). "
                            "Maximum morphospace distance (Euclidean ≈ 1.25) ensures rich intermediates.",
    },
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _apply_tradition(coords: dict, tradition: str) -> dict:
    """Apply tradition biases to coordinates, clamping to [0, 1]."""
    if tradition not in TRADITIONS:
        return coords
    biases = TRADITIONS[tradition]["biases"]
    return {p: _clamp(coords[p] + biases.get(p, 0.0)) for p in PARAMETER_NAMES}


def _euclidean_distance(a: dict, b: dict) -> float:
    return math.sqrt(sum((a[p] - b[p]) ** 2 for p in PARAMETER_NAMES))


def _interpolate(a: dict, b: dict, t: float) -> dict:
    return {p: a[p] + (b[p] - a[p]) * t for p in PARAMETER_NAMES}


def _check_affinity(coords: dict, affinity: dict) -> bool:
    """Check if coordinates fall within all affinity ranges."""
    for param, (low, high) in affinity.items():
        if param in coords:
            if coords[param] < low or coords[param] > high:
                return False
    return True


def _affinity_score(coords: dict, affinity: dict) -> float:
    """Score how well coordinates match affinity ranges. 1.0 = perfect center, 0.0 = outside."""
    if not affinity:
        return 0.5
    scores = []
    for param, (low, high) in affinity.items():
        if param in coords:
            val = coords[param]
            if val < low or val > high:
                return 0.0
            mid = (low + high) / 2.0
            half_range = (high - low) / 2.0
            if half_range > 0:
                scores.append(1.0 - abs(val - mid) / half_range)
            else:
                scores.append(1.0)
    return sum(scores) / len(scores) if scores else 0.5


def _match_visual_type(coords: dict) -> tuple:
    """Find best matching visual type for coordinates."""
    best_type = None
    best_dist = float("inf")
    for type_id, vt in VISUAL_TYPES.items():
        dist = _euclidean_distance(coords, vt["center"])
        if dist < best_dist:
            best_dist = dist
            best_type = type_id
    return best_type, best_dist


def _extract_vocabulary(coords: dict) -> dict:
    """Deterministic vocabulary extraction from coordinates."""
    result = {
        "compositions": [],
        "surfaces": [],
        "motifs": [],
        "color_registers": [],
        "figure_treatments": [],
    }

    for name, comp in COMPOSITIONAL_STRUCTURES.items():
        if _check_affinity(coords, comp["affinity"]):
            score = _affinity_score(coords, comp["affinity"])
            result["compositions"].append({"id": name, "specification": comp["specification"], "score": round(score, 3)})

    for name, surf in SURFACE_TREATMENTS.items():
        if _check_affinity(coords, surf["affinity"]):
            score = _affinity_score(coords, surf["affinity"])
            result["surfaces"].append({"id": name, "specification": surf["specification"], "score": round(score, 3)})

    for name, motif in ORNAMENTAL_MOTIFS.items():
        if _check_affinity(coords, motif["affinity"]):
            score = _affinity_score(coords, motif["affinity"])
            result["motifs"].append({"id": name, "keywords": motif["keywords"], "score": round(score, 3)})

    for name, cr in COLOR_REGISTERS.items():
        if _check_affinity(coords, cr["affinity"]):
            score = _affinity_score(coords, cr["affinity"])
            result["color_registers"].append({"id": name, "palette": cr["palette"], "score": round(score, 3)})

    for name, ft in FIGURE_TREATMENTS.items():
        if _check_affinity(coords, ft["affinity"]):
            score = _affinity_score(coords, ft["affinity"])
            result["figure_treatments"].append({"id": name, "specification": ft["specification"], "score": round(score, 3)})

    # Sort each by score descending
    for key in result:
        result[key].sort(key=lambda x: x["score"], reverse=True)

    return result


def _get_optical_properties(coords: dict) -> dict:
    """Get optical properties for coordinates."""
    result = {}
    prec = coords.get("material_preciousness", 0.5)
    for entry in OPTICAL_PROPERTIES["reflectance_by_preciousness"]:
        low, high = entry["range"]
        if low <= prec <= high:
            result["reflectance"] = entry["behavior"]
            break

    dens = coords.get("ornamental_density", 0.5)
    for entry in OPTICAL_PROPERTIES["depth_by_density"]:
        low, high = entry["range"]
        if low <= dens <= high:
            result["depth"] = entry["behavior"]
            break

    return result


def _decompose_intent(description: str) -> dict:
    """Decompose natural language into 5D coordinates via keyword matching."""
    tokens = set(description.lower().replace(",", " ").replace(".", " ").split())
    matches = []

    for type_id, vt in VISUAL_TYPES.items():
        overlap = tokens & set(vt["keywords"])
        if overlap:
            matches.append({
                "type_id": type_id,
                "score": len(overlap),
                "matched_keywords": sorted(overlap),
                "coordinates": vt["center"],
                "optical": vt["optical"],
                "color_associations": vt["color_associations"],
            })

    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches


# =============================================================================
# PHASE 2.6 COMPUTATION HELPERS (Layer 2 — zero LLM cost)
# =============================================================================

def _generate_oscillation(num_steps: int, num_cycles: float, pattern: str) -> list:
    """Generate oscillation alpha values [0.0 .. 1.0] for trajectory interpolation.

    Uses numpy-free math for minimal dependencies.
    """
    values = []
    for i in range(num_steps):
        t = 2.0 * math.pi * num_cycles * i / num_steps
        if pattern == "sinusoidal":
            values.append(0.5 * (1.0 + math.sin(t)))
        elif pattern == "triangular":
            t_norm = (t / (2.0 * math.pi)) % 1.0
            values.append(2.0 * t_norm if t_norm < 0.5 else 2.0 * (1.0 - t_norm))
        elif pattern == "square":
            t_norm = (t / (2.0 * math.pi)) % 1.0
            values.append(0.0 if t_norm < 0.5 else 1.0)
        else:
            values.append(0.5)
    return values


def _generate_preset_trajectory(preset_config: dict) -> list:
    """Generate full Phase 2.6 preset trajectory as list of coordinate dicts.

    Returns list of length (num_cycles × steps_per_cycle), each entry a 5D dict.
    Forced-orbit integration: mathematically guaranteed periodic closure.
    """
    state_a_id = preset_config["state_a"]
    state_b_id = preset_config["state_b"]

    if state_a_id not in CANONICAL_STATES or state_b_id not in CANONICAL_STATES:
        return []

    coords_a = CANONICAL_STATES[state_a_id]["coordinates"]
    coords_b = CANONICAL_STATES[state_b_id]["coordinates"]

    total_steps = preset_config["num_cycles"] * preset_config["steps_per_cycle"]
    alphas = _generate_oscillation(total_steps, preset_config["num_cycles"], preset_config["pattern"])

    trajectory = []
    for alpha in alphas:
        point = {p: coords_a[p] + alpha * (coords_b[p] - coords_a[p]) for p in PARAMETER_NAMES}
        trajectory.append(point)

    return trajectory


def _trajectory_with_visual_types(trajectory: list) -> list:
    """Annotate trajectory points with nearest visual type and vocabulary."""
    annotated = []
    for i, point in enumerate(trajectory):
        vt, vt_dist = _match_visual_type(point)
        vt_data = VISUAL_TYPES.get(vt, {})
        annotated.append({
            "step": i,
            "coordinates": {p: round(point[p], 4) for p in PARAMETER_NAMES},
            "nearest_visual_type": vt,
            "type_distance": round(vt_dist, 4),
            "keywords": vt_data.get("keywords", []),
            "color_associations": vt_data.get("color_associations", []),
        })
    return annotated


# =============================================================================
# LAYER 1 TOOLS — Pure taxonomy lookup (0 tokens)
# =============================================================================

@mcp.tool()
def get_server_info() -> str:
    """Get server metadata and capabilities.

    Layer 1: Pure reference (0 tokens).
    """
    return json.dumps({
        "name": "vienna_secession_mcp",
        "description": "Five-dimensional aesthetic coordinate space for the Vienna Secession movement (1897-c.1910).",
        "version": "2.6.0",
        "dimensions": PARAMETER_NAMES,
        "n_visual_types": len(VISUAL_TYPES),
        "n_canonical_states": len(CANONICAL_STATES),
        "n_traditions": len(TRADITIONS),
        "n_compositional_structures": len(COMPOSITIONAL_STRUCTURES),
        "n_surface_treatments": len(SURFACE_TREATMENTS),
        "n_ornamental_motifs": len(ORNAMENTAL_MOTIFS),
        "n_color_registers": len(COLOR_REGISTERS),
        "n_figure_treatments": len(FIGURE_TREATMENTS),
        "n_cross_domain_trajectories": len(CROSS_DOMAIN_TRAJECTORIES),
        "layer_architecture": {
            "layer_1": "Pure taxonomy lookup (0 tokens)",
            "layer_2": "Deterministic computation incl. Phase 2.6/2.7 (0 tokens)",
            "layer_3": "Structured data for Claude synthesis (~100-200 tokens)",
        },
        "phase_2_6_enhancements": {
            "rhythmic_presets": True,
            "n_presets": len(RHYTHMIC_PRESETS),
            "periods": sorted(set(p["steps_per_cycle"] for p in RHYTHMIC_PRESETS.values())),
            "preset_names": sorted(RHYTHMIC_PRESETS.keys()),
            "forced_orbit_integration": True,
            "guaranteed_periodic_closure": True,
        },
        "phase_2_7_enhancements": {
            "attractor_visualization": True,
            "prompt_generation_modes": ["composite", "split_view", "sequence"],
            "rhythmic_sequence_generation": True,
            "supported_image_generators": ["stable_diffusion", "dall_e", "comfyui"],
        },
    }, indent=2)


@mcp.tool()
def get_canonical_states() -> str:
    """List all 11 canonical Vienna Secession aesthetic states with 5D coordinates.

    Layer 1: Pure taxonomy lookup (0 tokens).
    """
    return json.dumps(CANONICAL_STATES, indent=2)


@mcp.tool()
def get_card(card_name: str, tradition: str = "") -> str:
    """Look up a canonical state by name and return its complete visual specification.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Args:
        card_name: State name (e.g. 'golden_klimt', 'quadratl_hoffmann', 'ver_sacrum_print')
        tradition: Optional tradition to bias coordinates: klimt_painterly, hoffmann_geometric,
                   moser_graphic, olbrich_architectural, werkstatte_applied
    """
    if card_name not in CANONICAL_STATES:
        available = sorted(CANONICAL_STATES.keys())
        return json.dumps({"error": f"Unknown state '{card_name}'", "available_states": available})

    state = CANONICAL_STATES[card_name]
    coords = dict(state["coordinates"])
    if tradition:
        coords = _apply_tradition(coords, tradition)

    visual_type, type_dist = _match_visual_type(coords)
    vt_data = VISUAL_TYPES.get(visual_type, {})

    return json.dumps({
        "name": card_name,
        "tradition": tradition or "none",
        "coordinates": {p: round(coords[p], 3) for p in PARAMETER_NAMES},
        "description": state["description"],
        "primary_visual_type": visual_type,
        "visual_type_distance": round(type_dist, 4),
        "optical": vt_data.get("optical", {}),
        "color_associations": vt_data.get("color_associations", []),
        "compositional_geometry": _extract_vocabulary(coords)["compositions"][:3],
    }, indent=2)


@mcp.tool()
def get_traditions() -> str:
    """List available tradition biases with descriptions.

    Layer 1: Pure taxonomy lookup (0 tokens).
    """
    return json.dumps({
        tid: {"description": t["description"], "biases": t["biases"]}
        for tid, t in TRADITIONS.items()
    }, indent=2)


@mcp.tool()
def get_visual_types() -> str:
    """List all Vienna Secession visual types with keywords and optical properties.

    Layer 1: Pure taxonomy lookup (0 tokens).
    """
    result = {}
    for type_id, vt in VISUAL_TYPES.items():
        result[type_id] = {
            "keywords": vt["keywords"],
            "center": {p: round(v, 2) for p, v in vt["center"].items()},
            "optical": vt["optical"],
            "color_associations": vt["color_associations"],
        }
    return json.dumps(result, indent=2)


@mcp.tool()
def get_visual_vocabulary() -> str:
    """Return complete visual vocabulary organized by category.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Categories: compositional_structure, surface_treatment,
    ornamental_motif, color_register, figure_treatment.
    """
    return json.dumps({
        "compositional_structure": {
            name: {"specification": c["specification"], "keywords": c["keywords"]}
            for name, c in COMPOSITIONAL_STRUCTURES.items()
        },
        "surface_treatment": {
            name: {"specification": s["specification"], "keywords": s["keywords"]}
            for name, s in SURFACE_TREATMENTS.items()
        },
        "ornamental_motif": {
            name: {"keywords": m["keywords"]}
            for name, m in ORNAMENTAL_MOTIFS.items()
        },
        "color_register": {
            name: {"palette": cr["palette"]}
            for name, cr in COLOR_REGISTERS.items()
        },
        "figure_treatment": {
            name: {"specification": ft["specification"], "keywords": ft["keywords"]}
            for name, ft in FIGURE_TREATMENTS.items()
        },
    }, indent=2)


@mcp.tool()
def get_optical_properties() -> str:
    """Get optical property mappings — light interaction and depth behavior by coordinate ranges.

    Layer 1: Pure taxonomy lookup (0 tokens).
    """
    return json.dumps(OPTICAL_PROPERTIES, indent=2)


@mcp.tool()
def get_cross_domain_trajectories() -> str:
    """List cross-domain trajectory mappings to adjacent art movements.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Covers: Art Nouveau, Bauhaus, Byzantine, Japonisme, Arts & Crafts, Art Deco.
    """
    return json.dumps(CROSS_DOMAIN_TRAJECTORIES, indent=2)


# =============================================================================
# LAYER 2 TOOLS — Deterministic computation (0 tokens)
# =============================================================================

@mcp.tool()
def compute_card_distance(card_a: str, card_b: str) -> str:
    """Compute Euclidean distance between two states in 5D parameter space.

    Layer 2: Deterministic computation (0 tokens).

    Args:
        card_a: First state name
        card_b: Second state name
    """
    if card_a not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state '{card_a}'", "available": sorted(CANONICAL_STATES.keys())})
    if card_b not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state '{card_b}'", "available": sorted(CANONICAL_STATES.keys())})

    coords_a = CANONICAL_STATES[card_a]["coordinates"]
    coords_b = CANONICAL_STATES[card_b]["coordinates"]
    dist = _euclidean_distance(coords_a, coords_b)

    per_axis = {p: round(abs(coords_a[p] - coords_b[p]), 3) for p in PARAMETER_NAMES}
    max_axis = max(per_axis, key=per_axis.get)

    return json.dumps({
        "card_a": card_a,
        "card_b": card_b,
        "distance": round(dist, 4),
        "per_axis_distance": per_axis,
        "maximum_divergence_axis": max_axis,
    }, indent=2)


@mcp.tool()
def compute_card_trajectory(card_a: str, card_b: str, steps: int = 10) -> str:
    """Compute smooth trajectory between two states through 5D parameter space.

    Layer 2: Deterministic interpolation (0 tokens).

    Args:
        card_a: Starting state
        card_b: Target state
        steps: Number of interpolation steps (default 10)
    """
    if card_a not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state '{card_a}'"})
    if card_b not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state '{card_b}'"})

    coords_a = CANONICAL_STATES[card_a]["coordinates"]
    coords_b = CANONICAL_STATES[card_b]["coordinates"]

    trajectory = []
    for i in range(steps + 1):
        t = i / steps
        point = _interpolate(coords_a, coords_b, t)
        vt, vt_dist = _match_visual_type(point)
        trajectory.append({
            "step": i,
            "t": round(t, 3),
            "coordinates": {p: round(point[p], 3) for p in PARAMETER_NAMES},
            "nearest_visual_type": vt,
            "type_distance": round(vt_dist, 4),
        })

    return json.dumps({
        "card_a": card_a,
        "card_b": card_b,
        "steps": steps,
        "total_distance": round(_euclidean_distance(coords_a, coords_b), 4),
        "trajectory": trajectory,
    }, indent=2)


@mcp.tool()
def find_nearby_cards(card_name: str, max_results: int = 5) -> str:
    """Find canonical states nearest to the given state in 5D parameter space.

    Layer 2: Deterministic distance computation (0 tokens).

    Args:
        card_name: Reference state name
        max_results: Number of nearest neighbors to return (default 5)
    """
    if card_name not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state '{card_name}'"})

    ref_coords = CANONICAL_STATES[card_name]["coordinates"]
    distances = []
    for name, state in CANONICAL_STATES.items():
        if name == card_name:
            continue
        dist = _euclidean_distance(ref_coords, state["coordinates"])
        distances.append({"name": name, "distance": round(dist, 4), "description": state["description"]})

    distances.sort(key=lambda x: x["distance"])
    return json.dumps({
        "reference": card_name,
        "nearest": distances[:max_results],
    }, indent=2)


@mcp.tool()
def decompose_secession_intent(description: str) -> str:
    """Decompose natural language into Vienna Secession 5D coordinates via keyword matching.

    Layer 2: Deterministic classification (0 tokens).

    Args:
        description: Natural language description (e.g. 'golden mosaic byzantine sacred',
                     'minimal grid modern silver', 'flowing organic vine stained glass')

    Returns matching visual types ranked by keyword overlap score.
    """
    matches = _decompose_intent(description)
    if not matches:
        return json.dumps({
            "description": description,
            "matches": [],
            "note": "No keyword matches found. Try terms from visual type keywords.",
        })

    return json.dumps({
        "description": description,
        "n_matches": len(matches),
        "matches": matches,
        "best_coordinates": matches[0]["coordinates"] if matches else None,
    }, indent=2)


# =============================================================================
# PHASE 2.6 TOOLS — Rhythmic presets (Layer 2, 0 tokens)
# =============================================================================

@mcp.tool()
def list_vienna_secession_presets() -> str:
    """List all Phase 2.6 rhythmic presets with periods and state transitions.

    Layer 2: Pure lookup (0 tokens).

    Returns preset name, period, pattern, endpoint states, and
    period rationale for cross-domain composition planning.
    """
    result = {}
    for name, preset in RHYTHMIC_PRESETS.items():
        result[name] = {
            "period": preset["steps_per_cycle"],
            "pattern": preset["pattern"],
            "num_cycles": preset["num_cycles"],
            "total_steps": preset["num_cycles"] * preset["steps_per_cycle"],
            "state_a": preset["state_a"],
            "state_b": preset["state_b"],
            "description": preset["description"],
            "period_rationale": preset["period_rationale"],
        }
    return json.dumps({
        "domain": "vienna_secession",
        "phase": "2.6",
        "n_presets": len(result),
        "periods": sorted(set(p["steps_per_cycle"] for p in RHYTHMIC_PRESETS.values())),
        "presets": result,
    }, indent=2)


@mcp.tool()
def apply_vienna_secession_preset(
    preset_name: str,
    num_cycles: int = 0,
    steps_per_cycle: int = 0,
) -> str:
    """Apply a Phase 2.6 rhythmic preset, generating a complete oscillation trajectory.

    Layer 2: Deterministic forced-orbit integration (0 tokens).
    Mathematically guaranteed periodic closure — zero drift.

    Args:
        preset_name: One of the rhythmic preset names (e.g. 'golden_convergence',
                     'material_oscillation', 'epoch_sweep')
        num_cycles: Override default cycle count (0 = use preset default)
        steps_per_cycle: Override default steps per cycle / period (0 = use preset default)

    Returns full trajectory with per-step coordinates, nearest visual type,
    keywords, and color associations.
    """
    if preset_name not in RHYTHMIC_PRESETS:
        return json.dumps({
            "error": f"Unknown preset '{preset_name}'",
            "available": sorted(RHYTHMIC_PRESETS.keys()),
        })

    config = dict(RHYTHMIC_PRESETS[preset_name])
    if num_cycles > 0:
        config["num_cycles"] = num_cycles
    if steps_per_cycle > 0:
        config["steps_per_cycle"] = steps_per_cycle

    trajectory = _generate_preset_trajectory(config)
    if not trajectory:
        return json.dumps({"error": "Invalid state references in preset configuration"})

    annotated = _trajectory_with_visual_types(trajectory)

    # Compute visual-type transition summary
    vt_sequence = [step["nearest_visual_type"] for step in annotated]
    vt_unique = []
    for vt in vt_sequence:
        if not vt_unique or vt_unique[-1] != vt:
            vt_unique.append(vt)

    return json.dumps({
        "preset": preset_name,
        "period": config["steps_per_cycle"],
        "num_cycles": config["num_cycles"],
        "total_steps": len(annotated),
        "pattern": config["pattern"],
        "state_a": config["state_a"],
        "state_b": config["state_b"],
        "description": config["description"],
        "visual_type_sequence": vt_unique,
        "n_distinct_visual_regions": len(vt_unique),
        "trajectory": annotated,
    }, indent=2)


@mcp.tool()
def compute_vienna_secession_trajectory(
    state_a: str,
    state_b: str,
    steps_per_cycle: int = 20,
    num_cycles: int = 2,
    pattern: str = "sinusoidal",
) -> str:
    """Compute custom rhythmic trajectory between any two canonical states.

    Layer 2: Deterministic forced-orbit integration (0 tokens).

    Unlike apply_vienna_secession_preset (which uses curated presets),
    this tool lets you compose arbitrary oscillations between any pair
    of the 10 canonical states.

    Args:
        state_a: Starting canonical state name
        state_b: Target canonical state name
        steps_per_cycle: Steps per oscillation cycle (period)
        num_cycles: Number of complete cycles
        pattern: 'sinusoidal', 'triangular', or 'square'
    """
    if state_a not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state '{state_a}'", "available": sorted(CANONICAL_STATES.keys())})
    if state_b not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state '{state_b}'", "available": sorted(CANONICAL_STATES.keys())})
    if pattern not in ("sinusoidal", "triangular", "square"):
        return json.dumps({"error": f"Unknown pattern '{pattern}'", "available": ["sinusoidal", "triangular", "square"]})
    if steps_per_cycle < 4 or steps_per_cycle > 100:
        return json.dumps({"error": "steps_per_cycle must be between 4 and 100"})

    config = {
        "state_a": state_a,
        "state_b": state_b,
        "steps_per_cycle": steps_per_cycle,
        "num_cycles": num_cycles,
        "pattern": pattern,
    }

    trajectory = _generate_preset_trajectory(config)
    annotated = _trajectory_with_visual_types(trajectory)

    # Morphospace distance between endpoints
    dist = _euclidean_distance(
        CANONICAL_STATES[state_a]["coordinates"],
        CANONICAL_STATES[state_b]["coordinates"],
    )

    return json.dumps({
        "state_a": state_a,
        "state_b": state_b,
        "period": steps_per_cycle,
        "num_cycles": num_cycles,
        "total_steps": len(annotated),
        "pattern": pattern,
        "endpoint_distance": round(dist, 4),
        "trajectory": annotated,
    }, indent=2)


@mcp.tool()
def generate_rhythmic_vienna_secession_sequence(
    preset_name: str,
    mode: str = "composite",
    keyframe_count: int = 6,
) -> str:
    """Generate image-generation-ready prompt sequence from a rhythmic preset.

    Layer 2: Deterministic prompt generation (0 tokens).
    Phase 2.7 attractor visualization prompt generation.

    Samples keyframes from the preset trajectory and generates complete
    vocabulary + optical data for each, suitable for Stable Diffusion,
    DALL-E, or ComfyUI prompt sequences.

    Args:
        preset_name: Rhythmic preset name
        mode: 'composite' (blended prompt per frame),
              'split_view' (A/B contrast per frame),
              'sequence' (animation keyframes with interpolated orbits)
        keyframe_count: Number of evenly-spaced keyframes to extract (default 6)
    """
    if preset_name not in RHYTHMIC_PRESETS:
        return json.dumps({
            "error": f"Unknown preset '{preset_name}'",
            "available": sorted(RHYTHMIC_PRESETS.keys()),
        })

    config = RHYTHMIC_PRESETS[preset_name]
    trajectory = _generate_preset_trajectory(config)
    if not trajectory:
        return json.dumps({"error": "Failed to generate trajectory"})

    total = len(trajectory)
    # Sample evenly spaced keyframes
    if keyframe_count >= total:
        indices = list(range(total))
    else:
        indices = [round(i * (total - 1) / (keyframe_count - 1)) for i in range(keyframe_count)]

    keyframes = []
    for idx in indices:
        point = trajectory[idx]
        vt, vt_dist = _match_visual_type(point)
        vt_data = VISUAL_TYPES.get(vt, {})
        vocab = _extract_vocabulary(point)
        optical = _get_optical_properties(point)

        frame = {
            "keyframe_index": idx,
            "coordinates": {p: round(point[p], 4) for p in PARAMETER_NAMES},
            "nearest_visual_type": vt,
            "type_distance": round(vt_dist, 4),
            "keywords": vt_data.get("keywords", []),
            "color_associations": vt_data.get("color_associations", []),
            "optical_properties": optical,
            "compositions": [c["id"] for c in vocab["compositions"][:2]],
            "surfaces": [s["id"] for s in vocab["surfaces"][:2]],
            "motifs": [m["id"] for m in vocab["motifs"][:3]],
        }

        if mode == "split_view":
            inv = {p: _clamp(1.0 - point[p]) for p in PARAMETER_NAMES}
            inv_vt, _ = _match_visual_type(inv)
            inv_data = VISUAL_TYPES.get(inv_vt, {})
            frame["panel_b"] = {
                "coordinates": {p: round(inv[p], 4) for p in PARAMETER_NAMES},
                "nearest_visual_type": inv_vt,
                "keywords": inv_data.get("keywords", []),
            }

        keyframes.append(frame)

    return json.dumps({
        "preset": preset_name,
        "mode": mode,
        "period": config["steps_per_cycle"],
        "total_trajectory_steps": total,
        "keyframe_count": len(keyframes),
        "description": config["description"],
        "keyframes": keyframes,
    }, indent=2)


@mcp.tool()
def generate_attractor_prompt(coordinates: str, mode: str = "composite") -> str:
    """Generate image generation prompt vocabulary from 5D coordinates.

    Layer 2: Deterministic vocabulary extraction (0 tokens).

    Args:
        coordinates: JSON string of 5D coordinates, e.g.
            '{"geometric_rigidity": 0.8, "ornamental_density": 0.3, ...}'
        mode: 'composite' (single prompt), 'split_view' (two-panel), 'sequence' (animation frames)
    """
    try:
        coords = json.loads(coordinates)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON in coordinates"})

    for p in PARAMETER_NAMES:
        if p not in coords:
            return json.dumps({"error": f"Missing parameter: {p}", "required": PARAMETER_NAMES})

    vocabulary = _extract_vocabulary(coords)
    visual_type, vt_dist = _match_visual_type(coords)
    vt_data = VISUAL_TYPES.get(visual_type, {})
    optical = _get_optical_properties(coords)

    result = {
        "coordinates": {p: round(coords[p], 3) for p in PARAMETER_NAMES},
        "nearest_visual_type": visual_type,
        "type_distance": round(vt_dist, 4),
        "optical_properties": optical,
        "color_associations": vt_data.get("color_associations", []),
        "vocabulary": vocabulary,
        "mode": mode,
    }

    if mode == "split_view":
        # Generate contrasting coordinates for second panel
        inverted = {p: _clamp(1.0 - coords[p]) for p in PARAMETER_NAMES}
        inv_vocab = _extract_vocabulary(inverted)
        inv_vt, _ = _match_visual_type(inverted)
        result["panel_b"] = {
            "coordinates": {p: round(inverted[p], 3) for p in PARAMETER_NAMES},
            "nearest_visual_type": inv_vt,
            "vocabulary": inv_vocab,
        }
    elif mode == "sequence":
        # Generate 4 keyframes orbiting the coordinate
        frames = []
        for i in range(4):
            angle = i * math.pi / 2
            offset_coords = {
                p: _clamp(coords[p] + 0.1 * math.sin(angle + j * 0.5))
                for j, p in enumerate(PARAMETER_NAMES)
            }
            frame_vt, _ = _match_visual_type(offset_coords)
            frames.append({
                "frame": i,
                "coordinates": {p: round(offset_coords[p], 3) for p in PARAMETER_NAMES},
                "nearest_visual_type": frame_vt,
            })
        result["keyframes"] = frames

    return json.dumps(result, indent=2)


# =============================================================================
# LAYER 3 TOOL — Structured data for Claude synthesis (~100-200 tokens)
# =============================================================================

@mcp.tool()
def enhance_secession_prompt(
    intent: str,
    card_name: str = "",
    tradition: str = "",
    intensity: float = 0.7,
) -> str:
    """Full pipeline: intent + optional state + tradition → structured enhancement data.

    Layer 3: Provides structured data for Claude synthesis (~100-200 tokens).

    Args:
        intent: Natural language description of desired aesthetic
        card_name: Optional canonical state to anchor the enhancement
        tradition: Optional tradition (klimt_painterly, hoffmann_geometric, moser_graphic,
                   olbrich_architectural, werkstatte_applied)
        intensity: Enhancement intensity 0.0-1.0 (default 0.7)

    Returns complete structured data including coordinates, compositional geometry,
    visual vocabulary, optical properties, and color associations for Claude to
    synthesize into a final image generation prompt.
    """
    # Step 1: Determine base coordinates
    if card_name and card_name in CANONICAL_STATES:
        base_coords = dict(CANONICAL_STATES[card_name]["coordinates"])
    else:
        # Decompose intent to coordinates
        matches = _decompose_intent(intent)
        if matches:
            base_coords = dict(matches[0]["coordinates"])
        else:
            # Default to center of space
            base_coords = {p: 0.5 for p in PARAMETER_NAMES}

    # Step 2: Apply tradition bias
    if tradition:
        base_coords = _apply_tradition(base_coords, tradition)

    # Step 3: Apply intensity scaling (blend toward extremes)
    coords = {}
    for p in PARAMETER_NAMES:
        val = base_coords[p]
        if val > 0.5:
            coords[p] = _clamp(val + (val - 0.5) * intensity * 0.5)
        else:
            coords[p] = _clamp(val - (0.5 - val) * intensity * 0.5)

    # Step 4: Extract all vocabulary
    vocabulary = _extract_vocabulary(coords)
    visual_type, vt_dist = _match_visual_type(coords)
    vt_data = VISUAL_TYPES.get(visual_type, {})
    optical = _get_optical_properties(coords)

    # Step 5: Get intent decomposition for keyword context
    intent_matches = _decompose_intent(intent)

    # Step 6: Assemble structured output
    return json.dumps({
        "intent": intent,
        "card_name": card_name or "none",
        "tradition": tradition or "none",
        "intensity": intensity,
        "coordinates": {p: round(coords[p], 3) for p in PARAMETER_NAMES},
        "primary_visual_type": visual_type,
        "visual_type_distance": round(vt_dist, 4),
        "optical_properties": optical,
        "color_associations": vt_data.get("color_associations", []),
        "intent_keywords_matched": [
            {"type": m["type_id"], "score": m["score"], "keywords": m["matched_keywords"]}
            for m in intent_matches[:3]
        ],
        "compositional_geometry": vocabulary["compositions"][:3],
        "surface_treatments": vocabulary["surfaces"][:3],
        "ornamental_motifs": vocabulary["motifs"][:4],
        "color_registers": vocabulary["color_registers"][:2],
        "figure_treatments": vocabulary["figure_treatments"][:2],
        "cross_domain_trajectories": {
            tid: t["interpolation_character"]
            for tid, t in CROSS_DOMAIN_TRAJECTORIES.items()
        },
    }, indent=2)


# =============================================================================
# DOMAIN REGISTRY — for aesthetics-dynamics-core composition
# =============================================================================

@mcp.tool()
def get_domain_registry_config() -> str:
    """Return Tier 4D integration configuration for compositional limit cycles.

    Layer 2: Pure lookup (0 tokens).

    Returns the domain signature for registering with the
    aesthetic-dynamics-core compositional system, including Phase 2.6
    preset configurations and predicted emergent attractors.
    """
    preset_configs = {}
    for name, preset in RHYTHMIC_PRESETS.items():
        coords_a = CANONICAL_STATES[preset["state_a"]]["coordinates"]
        coords_b = CANONICAL_STATES[preset["state_b"]]["coordinates"]
        preset_configs[name] = {
            "period": preset["steps_per_cycle"],
            "pattern": preset["pattern"],
            "state_a_coords": coords_a,
            "state_b_coords": coords_b,
        }

    return json.dumps({
        "domain_id": "vienna_secession",
        "display_name": "Vienna Secession Aesthetics",
        "parameter_names": PARAMETER_NAMES,
        "parameter_ranges": {p: [0.0, 1.0] for p in PARAMETER_NAMES},
        "n_visual_types": len(VISUAL_TYPES),
        "n_canonical_states": len(CANONICAL_STATES),
        "canonical_state_coordinates": {
            name: state["coordinates"]
            for name, state in CANONICAL_STATES.items()
        },
        "visual_type_centers": {
            type_id: vt["center"]
            for type_id, vt in VISUAL_TYPES.items()
        },
        "visual_type_keywords": {
            type_id: vt["keywords"]
            for type_id, vt in VISUAL_TYPES.items()
        },
        "phase_2_6": {
            "presets": preset_configs,
            "periods": sorted(set(p["steps_per_cycle"] for p in RHYTHMIC_PRESETS.values())),
        },
        "predicted_emergent_attractors": {
            "period_14_gap_filler": {
                "mechanism": "Gap-filler: fills 12-15 period gap",
                "predicted_basin_size": 0.03,
                "confidence": "medium",
                "note": "Novel period. LCM(14,12)=84, LCM(14,15)=210 create new harmonics.",
            },
            "period_30_lcm_reinforcement": {
                "mechanism": "LCM hub reinforcement: vienna_secession joins microscopy+diatom+heraldic at Period 30",
                "predicted_basin_size": 0.12,
                "confidence": "high",
                "note": "Adding 4th domain to Period 30 hub should strengthen dominance.",
            },
            "period_28_composite_reinforcement": {
                "mechanism": "Composite beat reinforcement: epoch_sweep at Period 28 aligns with 60-2×16",
                "predicted_basin_size": 0.06,
                "confidence": "medium",
                "note": "May partially restore Period 28 basin weakened in 5-domain system.",
            },
            "period_22_cross_domain": {
                "mechanism": "Triple-lock: vienna_secession+catastrophe+heraldic at Period 22",
                "predicted_basin_size": 0.04,
                "confidence": "medium",
                "note": "Triangular pattern may create distinctive transition dynamics.",
            },
        },
    }, indent=2)

if __name__ == "__main__":
    mcp.run()
