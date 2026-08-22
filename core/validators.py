import os

from django.conf import settings
from django.core.exceptions import ValidationError


def validate_document_file(value):
    """
    Inazuia:
    1. Faili zenye kiendelezi (extension) kisichoruhusiwa - epuka .exe, .php, .html n.k.
    2. Faili kubwa kupita kiasi (kinga dhidi ya mashambulizi ya 'denial of service' kwa
       kujaza hifadhi/kumbukumbu ya server).
    Kumbuka: haya ni ukaguzi wa awali tu (extension + size). Kwa ulinzi wa ziada
    kwenye uzalishaji mkubwa, ongeza uchunguzi wa 'magic bytes' (mfano: python-magic)
    kuhakiki maudhui halisi ya faili yanaendana na kiendelezi chake.
    """
    ext = os.path.splitext(value.name)[1].lower()
    allowed = getattr(settings, "ALLOWED_UPLOAD_EXTENSIONS", [".pdf", ".doc", ".docx"])
    if ext not in allowed:
        raise ValidationError(
            f"Aina ya faili '{ext}' haikubaliki. Tumia mojawapo ya: {', '.join(allowed)}"
        )

    max_size = getattr(settings, "MAX_UPLOAD_SIZE_BYTES", 5 * 1024 * 1024)
    if value.size > max_size:
        raise ValidationError(
            f"Faili ni kubwa mno. Kiwango cha juu ni {max_size // (1024 * 1024)}MB."
        )
