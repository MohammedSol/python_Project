from django.db import models
from django.contrib.auth.models import User


class Salle(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    equipements = models.TextField(help_text="Ex: Vidéoprojecteur, Wi-Fi, Tableau blanc")
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()

    def __str__(self):
        return self.nom


class Reservation(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField(null=True, blank=True)
    motif = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.salle.nom} - {self.date}"


# Historique pour garder une trace
class HistoriqueReservation(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    date_modification = models.DateTimeField(auto_now=True)
    details = models.TextField()

    def __str__(self):
        return f"Historique de {self.reservation}"
