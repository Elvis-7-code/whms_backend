from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    # Create database tables if they don't exist
    db.create_all()
    
    # Create admin user
    admin = User(
        name="Farm Admin",
        email="admin@farm.com",
        role="owner"
    )
    admin.set_password("admin123")  # Change this!
    
    # Create manager
    manager = User(
        name="Farm Manager",
        email="manager@farm.com",
        role="manager"
    )
    manager.set_password("manager123")  # Change this!
    
    # Create worker
    worker = User(
        name="Farm Worker",
        email="worker@farm.com",
        role="worker"
    )
    worker.set_password("worker123")  # Change this!
    
    # Add all users
    db.session.add(admin)
    db.session.add(manager)
    db.session.add(worker)
    
    try:
        db.session.commit()
        print("✅ Users created successfully!")
        print("\nLogin credentials:")
        print("Admin: admin@farm.com / admin123")
        print("Manager: manager@farm.com / manager123")
        print("Worker: worker@farm.com / worker123")
    except Exception as e:
        print(f"❌ Error: {e}")
        db.session.rollback()