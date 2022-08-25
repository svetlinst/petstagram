from django.core.exceptions import ValidationError


def validate_alpha_chars_only(value):
    if not value.isalpha():
        raise ValidationError('Value must contain only letters.')


def validate_photo_max_size(max_size):
    def file_size(value):
        limit = max_size * 1024 * 1024
        if value.file.size > limit:
            raise ValidationError('File too large.')
    return file_size
