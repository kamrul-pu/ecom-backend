from projectile.settings import VERSATILEIMAGEFIELD_RENDITION_KEY_SETS

validate_product_image = {
    "type": "object",
    "properties": {
        key: {"type": "string", "format": "uri"}
        for key, _ in VERSATILEIMAGEFIELD_RENDITION_KEY_SETS.get("product_images", [])
    },
    "required": [
        key
        for key, _ in VERSATILEIMAGEFIELD_RENDITION_KEY_SETS.get("product_images", [])
    ],
    "additionalProperties": False,
}
